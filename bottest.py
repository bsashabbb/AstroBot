from tg_api.client import TelegramClient
from tg_api.models import User, Chat, Message
from tg_api.methods import BotAPI
import asyncio

class MyBot(BotAPI):
    async def get_me_info(self):
        """Пример кастомного метода"""
        response = await self.get_me()
        return User(**response['result'])

    async def send_hello(self, chat_id: int):
        """Пример отправки сообщения"""
        return await self.send_message(
            chat_id=chat_id,
            text="Hello from generated library!",
            parse_mode="Markdown"
        )

async def main():
    async with MyBot("7562422490:AAHdV8dwIb2kQO7A9DVPrW7L2bnVcoCE0IQ") as bot:
        # Получение информации о боте
        me = await bot.get_me_info()
        print(f"Bot ID: {me.id}, Username: @{me.username}")

        # Отправка сообщения
        sent_message = await bot.send_hello(chat_id=me.id)
        message_obj = Message(**sent_message['result'])
        
        # Работа с объектами
        print(f"Sent message ID: {message_obj.message_id}")
        print(f"Message content: {message_obj.text}")
        
        # Конвертация в словарь
        print("Message as dict:", message_obj.to_dict())

        # Проверка типов
        try:
            message_obj.message_id = "invalid_id"  # Вызовет TypeError
        except TypeError as e:
            print(f"Type check worked: {e}")

if __name__ == "__main__":
    asyncio.run(main())