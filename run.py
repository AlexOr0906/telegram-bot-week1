import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
quotes = [
    "Код — это поэзия.",
    "Ошибки — это уроки.",
    "Python — это магия."
]

jokes=["Почему программист не любит природу? Там полно багов, и нет Ctrl+Z!",
"Как программист чинит лампочку? Перезагружает дом.",
"Сколько программистов нужно, чтобы вкрутить лампочку? Ни одного — это аппаратная проблема.",
"Почему Python так популярен? Потому что он не требует скобок и не судит за отступы.",
"Что говорит программист, когда его код не работает?'Это не баг — это фича!'",

]
# ←←← ВСТАВЬ СВОЙ ТОКЕН СЮДА (от @BotFather)
bot = Bot(token="8570222001:AAE7AwJMtPhTSTOmDlmNuK3Q6Pe-aSi8Ckg")
dp = Dispatcher()

@dp.message(Command('joke'))
async def send_joke(message: types.Message):
    await message.reply(random.choice(jokes))

@dp.message(Command('quote'))
async def send_auote(message: types.Message):
    await message.reply(random.choice(quotes))

@dp.message(Command("info"))
async def send_info(message: types.Message):
    await message.reply("Я создан для изучения Python и кибербезопасности.")

@dp.message(Command("help"))
async def send_help(message: types.Message):
    await message.reply("Я-бот, пиши /strart или /info")

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Hello!")

if __name__ == '__main__':
    print("Бот запущен...")
    dp.run_polling(bot)