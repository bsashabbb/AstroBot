import re
import httpx
import asyncio
from typing import (
    Callable,
    Awaitable,
    Optional,
    Union,
    List,
    Any,
    Pattern,
    Coroutine
)
from .types import Update, Message, CallbackQuery, ChatMember, User

class AstroBot:
    def __init__(self, token: str):
        self.token = token
        self.client = httpx.AsyncClient()
        self.base_url = f"https://api.telegram.org/bot{self.token}"

        # Регистрация обработчиков
        self.message_handlers = []
        self.callback_handlers = []
        self.inline_handlers = []

        # Состояние бота
        self.update_offset = None
        self.running = False

    async def start(self):
        """Запуск основного цикла бота"""
        self.running = True
        while self.running:
            try:
                updates = await self.get_updates(offset=self.update_offset, timeout=30)
                for update in updates.get("result", []):
                    await self.handle_update(Update(**update))
                    self.update_offset = update["update_id"] + 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Ошибка: {e}")
                await asyncio.sleep(5)

    async def get_updates(self, offset: Optional[int] = None, timeout: int = 30):
        """Получение обновлений от Telegram API"""
        params = {"timeout": timeout}
        if offset is not None:
            params["offset"] = offset

        response = await self.client.get(
            f"{self.base_url}/getUpdates",
            params=params
        )
        return response.json()

    async def handle_update(self, update: Update):
        """Обработка входящего обновления"""
        if update.message:
            await self._process_message(update.message)
        if update.callback_query:
            await self._process_callback(update.callback_query)

    async def _process_message(self, message: Message):
        """Обработка входящего сообщения"""
        for handler in self.message_handlers:
            if await self._check_message_filters(message, handler["filters"]):
                await handler["func"](message)
                break

    async def _process_callback(self, callback: CallbackQuery):
        """Обработка колбэк-запроса"""
        for handler in self.callback_handlers:
            if await self._check_callback_filters(callback, handler["filters"]):
                await handler["func"](callback)
                break

    def message_handler(
            self,
            commands: Optional[List[str]] = None,
            content_types: Optional[List[str]] = None,
            regex: Optional[Union[str, Pattern]] = None,
            is_admin: bool = False,
            func: Optional[Callable[[Message], Union[bool, Awaitable[bool]]]] = None
    ) -> Callable:
        """Декоратор для обработки сообщений"""
        def decorator(handler_func: Callable[[Message], Awaitable[None]]):
            filters = {
                "commands": commands,
                "content_types": content_types,
                "regex": re.compile(regex) if isinstance(regex, str) else regex,
                "is_admin": is_admin,
                "custom_func": func
            }
            self.message_handlers.append({
                "func": handler_func,
                "filters": filters
            })
            return handler_func
        return decorator

    def callback_query_handler(
            self,
            data: Optional[str] = None,
            pattern: Optional[Union[str, Pattern]] = None,
            func: Optional[Callable[[CallbackQuery], Union[bool, Awaitable[bool]]]] = None
    ) -> Callable:
        """Декоратор для обработки колбэков"""
        def decorator(handler_func: Callable[[CallbackQuery], Awaitable[None]]):
            filters = {
                "data": data,
                "pattern": re.compile(pattern) if isinstance(pattern, str) else pattern,
                "custom_func": func
            }
            self.callback_handlers.append({
                "func": handler_func,
                "filters": filters
            })
            return handler_func
        return decorator

    async def _check_message_filters(self, message: Message, filters: dict) -> bool:
        """Проверка фильтров для сообщения"""
        checks = []

        # Проверка команд
        if filters["commands"]:
            checks.append(await self._check_commands(message, filters["commands"]))

        # Проверка типов контента
        if filters["content_types"]:
            checks.append(message.content_type in filters["content_types"])

        # Проверка регулярных выражений
        if filters["regex"] and message.text:
            checks.append(filters["regex"].search(message.text) is not None)

        # Проверка прав администратора
        if filters["is_admin"]:
            checks.append(await self._is_admin(message))

        # Пользовательская функция-фильтр
        if filters["custom_func"]:
            result = filters["custom_func"](message)
            if isinstance(result, Coroutine):
                result = await result
            checks.append(result)

        return all(checks)

    async def _check_callback_filters(self, callback: CallbackQuery, filters: dict) -> bool:
        """Проверка фильтров для колбэков"""
        checks = []

        # Точное совпадение данных
        if filters["data"]:
            checks.append(callback.data == filters["data"])

        # Проверка по регулярному выражению
        if filters["pattern"] and callback.data:
            checks.append(filters["pattern"].search(callback.data) is not None)

        # Пользовательская функция-фильтр
        if filters["custom_func"]:
            result = filters["custom_func"](callback)
            if isinstance(result, Coroutine):
                result = await result
            checks.append(result)

        return all(checks)

    async def _check_commands(self, message: Message, commands: List[str]) -> bool:
        """Проверка соответствия командам"""
        if message.text and message.text.startswith('/'):
            command = message.text.split()[0][1:].split('@')[0]
            return command in commands
        return False

    async def _is_admin(self, message: Message) -> bool:
        """Проверка прав администратора"""
        if not message.from_user or not message.chat:
            return False

        member = await self.get_chat_member(
            chat_id=message.chat.id,
            user_id=message.from_user.id
        )
        return member.status in ["creator", "administrator"]

    async def get_chat_member(self, chat_id: int, user_id: int) -> ChatMember:
        """Получение информации о участнике чата"""
        response = await self.client.post(
            f"{self.base_url}/getChatMember",
            json={"chat_id": chat_id, "user_id": user_id}
        )
        return ChatMember(**response.json()["result"])

    async def send_message(self, chat_id: int, text: str, **kwargs) -> Message:
        """Отправка сообщения"""
        response = await self.client.post(
            f"{self.base_url}/sendMessage",
            json={"chat_id": chat_id, "text": text, **kwargs}
        )
        return Message(**response.json()["result"])

    async def answer_callback_query(self, callback_id: str, **kwargs):
        """Ответ на колбэк-запрос"""
        await self.client.post(
            f"{self.base_url}/answerCallbackQuery",
            json={"callback_query_id": callback_id, **kwargs}
        )

    async def close(self):
        """Остановка бота"""
        self.running = False
        await self.client.aclose()