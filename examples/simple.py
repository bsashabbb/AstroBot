import asyncio
from typing import Dict, Optional, Callable, Awaitable
from astrobot import AstroBot
from astrobot.types import Message, CallbackQuery, Update


class FSM:
    def __init__(self):
        self.states: Dict[int, str] = {}
        self.data: Dict[int, Dict] = {}

    async def get_state(self, user_id: int) -> Optional[str]:
        return self.states.get(user_id)

    async def set_state(self, user_id: int, state: str):
        self.states[user_id] = state

    async def reset_state(self, user_id: int):
        if user_id in self.states:
            del self.states[user_id]
        if user_id in self.data:
            del self.data[user_id]

    async def update_data(self, user_id: int, **kwargs):
        if user_id not in self.data:
            self.data[user_id] = {}
        self.data[user_id].update(kwargs)

    async def get_data(self, user_id: int) -> Dict:
        return self.data.get(user_id, {})


class AstroBotFSM(AstroBot):
    def __init__(self, token: str):
        super().__init__(token)
        self.fsm = FSM()

    def state_handler(self, state: str) -> Callable:
        def decorator(func: Callable[[Message], Awaitable[None]]):
            async def wrapper(update: Update):
                if not update.message:
                    return
                msg = update.message
                current_state = await self.fsm.get_state(msg.from_user.id)
                if current_state == state:
                    await func(msg)

            self.message_handlers.append(wrapper)
            return func

        return decorator


# Пример использования
bot = AstroBotFSM("7562422490:AAHdV8dwIb2kQO7A9DVPrW7L2bnVcoCE0IQ")


# Стартовая команда
@bot.message_handler(commands=['start'])
async def start_handler(message: Message):
    await bot.fsm.set_state(message.from_.id, "name_input")
    await message.reply("Введите ваше имя:")


# Обработчик состояния ввода имени
@bot.state_handler("name_input")
async def process_name(message: Message):
    await bot.fsm.update_data(message.from_.id, name=message.text)
    await bot.fsm.set_state(message.from_.id, "age_input")
    await message.reply("Теперь введите ваш возраст:")


# Обработчик состояния ввода возраста
@bot.state_handler("age_input")
async def process_age(message: Message):
    if not message.text.isdigit():
        await message.reply("Возраст должен быть числом!")
        return

    await bot.fsm.update_data(message.from_.id, age=int(message.text))
    await bot.fsm.set_state(message.from_.id, "confirm")

    data = await bot.fsm.get_data(message.from_.id)
    await message.reply(
        f"Проверьте данные:\nИмя: {data['name']}\nВозраст: {data['age']}\n"
        "Всё верно? (да/нет)"
    )


# Обработчик подтверждения
@bot.state_handler("confirm")
async def process_confirm(message: Message):
    if message.text.lower() == 'да':
        data = await bot.fsm.get_data(message.from_.id)
        await message.reply(
            "Данные сохранены!\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}"
        )
    else:
        await message.reply("Начнём заново!")

    await bot.fsm.reset_state(message.from_.id)


# Запуск бота
if __name__ == "__main__":
    asyncio.run(bot.start())
