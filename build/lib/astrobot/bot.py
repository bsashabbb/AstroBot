import asyncio
import httpx
import logging
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any, Callable, Awaitable
from .types import *


class AstroBot:
    def __init__(self, token: str, log_to_file: bool = False, log_chat_id: Optional[int] = None) -> None:
        """
        Инициализация бота.

        :param token: Токен вашего Telegram бота.
        :param log_to_file: Если True, логи будут записываться в файл.
        :param log_chat_id: ID чата для отправки логов. Если None, логи в чат не отправляются.
        """
        self.token: str = token
        self.client: httpx.AsyncClient = httpx.AsyncClient()  # HTTP-клиент для запросов
        self.base_url: str = f"https://api.telegram.org/bot{self.token}"
        self.update_offset: Optional[int] = None  # Смещение для получения обновлений
        self.scheduled_messages: List[ScheduledMessage] = []  # Список запланированных сообщений
        self.handlers: List[Callable[[Update], Awaitable[None]]] = []  # Список обработчиков
        self.log_chat_id: Optional[int] = log_chat_id  # ID чата для логирования

        # Настройка логирования
        self.logger: logging.Logger = logging.getLogger("AstroBot")
        self.logger.setLevel(logging.INFO)  # Уровень логирования

        # Формат сообщений
        formatter: logging.Formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Логирование в консоль
        console_handler: logging.StreamHandler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Логирование в файл (если включено)
        if log_to_file:
            file_handler: logging.FileHandler = logging.FileHandler("astrobot.log")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    async def start(self) -> None:
        """
        Запуск бота. Основной цикл работает до ошибки, а второй цикл логирует ошибки и продолжает работу.
        """
        self.logger.info("Бот запущен! 🚀")
        asyncio.create_task(self._check_scheduled_messages())  # Запуск задачи для проверки запланированных сообщений
        while True:
            try:
                # Основной цикл
                await self.main_loop()
            except Exception as e:
                # Логируем ошибку и продолжаем работу
                self.logger.info(f"Произошла ошибка в основном цикле: {e}")
                await self.log_to_chat(f"Ошибка в основном цикле: {e}")
                await asyncio.sleep(5)  # Пауза перед повторным запуском

    async def main_loop(self) -> None:
        """
        Основной цикл бота. Работает до тех пор, пока не произойдет ошибка.
        """
        while True:
            try:
                # Получаем обновления от Telegram API
                updates: TelegramResponse = await self.get_updates(offset=self.update_offset, timeout=60)

                # Обрабатываем каждое обновление
                for update in updates.get("result", []):
                    await self.handle_update(update)
                    # Обновляем offset, чтобы не обрабатывать одно и то же обновление дважды
                    self.update_offset = update["update_id"] + 1

                # Небольшая пауза, чтобы не нагружать сервер
                await asyncio.sleep(1)
            except Exception as e:
                # Логируем ошибку и продолжаем работу
                self.logger.info(f"Ошибка при обработке обновлений: {e}")
                await self.log_to_chat(f"Ошибка при обработке обновлений: {e}")
                await asyncio.sleep(5)  # Пауза перед повторной попыткой

    async def get_updates(self, offset: Optional[int] = None, timeout: int = 60) -> TelegramResponse:
        """
        Получение обновлений от Telegram API.

        :param offset: Смещение для получения обновлений.
        :param timeout: Таймаут для long polling.
        :return: Список обновлений.
        """
        params: Dict[str, Any] = {"timeout": timeout}
        if offset is not None:
            params["offset"] = offset

        # Отправляем запрос к Telegram API
        response: httpx.Response = await self.client.get(f"{self.base_url}/getUpdates", params=params)
        response.raise_for_status()  # Проверяем, что запрос успешен
        return response.json()

    async def handle_update(self, update: Update) -> None:
        """
        Метод для обработки обновления. Вызывает все зарегистрированные обработчики.
        """
        # Логируем обновление
        self.logger.info(f"Получено обновление: {update}")
        await self.log_to_chat(f"Получено обновление: {update}")

        # Вызываем все зарегистрированные обработчики
        for handler in self.handlers:
            await handler(update)

    def register_handler(self, handler: Callable[[Update], Awaitable[None]]) -> None:
        """
        Регистрация обработчика через функцию.

        :param handler: Функция-обработчик обновлений.
        """
        self.handlers.append(handler)

    def message_handler(self, func: Callable[[Update], Awaitable[None]]) -> Callable[[Update], Awaitable[None]]:
        """
        Декоратор для регистрации обработчика сообщений.

        :param func: Функция-обработчик обновлений.
        """
        self.register_handler(func)
        return func

    async def send_message(self, chat_id: int, text: str, **kwargs: Any) -> TelegramResponse:
        """
        Отправка сообщения.

        :param chat_id: ID чата.
        :param text: Текст сообщения.
        :param kwargs: Дополнительные параметры.
        :return: Ответ от Telegram API.
        """
        data: Dict[str, Any] = {"chat_id": chat_id, "text": text, **kwargs}
        response: httpx.Response = await self.client.post(f"{self.base_url}/sendMessage", json=data)
        response.raise_for_status()
        return response.json()

    async def log_to_chat(self, message: str) -> None:
        """
        Отправка лога в указанный чат.

        :param message: Текст сообщения для логирования.
        """
        if self.log_chat_id:
            try:
                await self.send_message(self.log_chat_id, f"📝 Лог: {message}")
            except Exception as e:
                self.logger.error(f"Ошибка при отправке лога в чат: {e}")

    async def schedule_message(self, chat_id: int, text: str, send_at: datetime) -> None:
        """
        Запланировать отправку сообщения на определенное время.

        :param chat_id: ID чата.
        :param text: Текст сообщения.
        :param send_at: Дата и время отправки сообщения.
        """
        self.scheduled_messages.append({
            "chat_id": chat_id,
            "text": text,
            "send_at": send_at
        })
        self.logger.info(f"Сообщение добавлено в очередь на {send_at}")
        await self.log_to_chat(f"Сообщение добавлено в очередь на {send_at}")

    async def _check_scheduled_messages(self) -> None:
        """
        Фоновая задача для проверки и отправки запланированных сообщений.
        """
        while True:
            now: datetime = datetime.now()
            for message in self.scheduled_messages[:]:  # Используем срез для безопасного удаления
                if now >= message["send_at"]:
                    try:
                        await self.send_message(message["chat_id"], message["text"])
                        self.scheduled_messages.remove(message)  # Удаляем отправленное сообщение
                        self.logger.info(f"Сообщение отправлено в {now}")
                        await self.log_to_chat(f"Сообщение отправлено в {now}")
                    except Exception as e:
                        self.logger.info(f"Ошибка при отправке запланированного сообщения: {e}")
                        await self.log_to_chat(f"Ошибка при отправке запланированного сообщения: {e}")
            await asyncio.sleep(1)  # Проверяем каждую секунду

    async def close(self) -> None:
        """
        Закрытие бота и освобождение ресурсов.
        """
        await self.client.aclose()
        self.logger.info("Бот завершил работу.")
        await self.log_to_chat("Бот завершил работу.")
