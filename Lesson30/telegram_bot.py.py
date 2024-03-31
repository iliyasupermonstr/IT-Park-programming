from aiogram import Bot, Dispatcher, types
import asyncio

# Указываем ваш токен Telegram
TOKEN = '6858600007:AAEtdYrEDVDu2wGpm7E0NHMq_Si-Bhh9MYM'

# Создаем экземпляр бота
bot = Bot(token=TOKEN)

# Создаем экземпляр диспетчера
dp = Dispatcher()

# Связываем диспетчер с ботом
dp.bind(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Создаем клавиатуру с кнопкой для открытия веб-страницы
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть страницу', url='https://www.example.com'))
    
    # Отправляем пользователю приветственное сообщение с клавиатурой
    await message.answer('Привет! Нажми на кнопку, чтобы открыть веб-страницу.', reply_markup=markup)

# Функция запуска бота
async def main():
    # Стартуем бота
    await dp.start_polling()

# Запускаем бота
if __name__ == '__main__':
    asyncio.run(main())
