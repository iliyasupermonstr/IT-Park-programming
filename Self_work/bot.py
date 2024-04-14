import telebot
import sqlite3
from telebot import types
import config

# Замените 'YOUR_TOKEN' на ваш токен от BotFather
TOKEN = config.TOKEN
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Этот бот поможет тебе учесть долги. "
                          "Чтобы добавить долг, напиши /add_debt")

# Обработчик команды /add_debt
@bot.message_handler(commands=['add_debt'])
def add_debt(message):
    msg = bot.reply_to(message, "Введите ID друга:")
    bot.register_next_step_handler(msg, process_debtor_id_step)

def process_debtor_id_step(message):
    debtor_id = message.text
    if debtor_id.isdigit():
        debtor_id = int(debtor_id)
        msg = bot.reply_to(message, "Введите сумму долга:")
        bot.register_next_step_handler(msg, lambda msg: process_amount_step(msg, debtor_id))
    else:
        bot.reply_to(message, "ID должен быть числом")

def process_amount_step(message, debtor_id):
    amount = message.text
    msg = bot.reply_to(message, "Введите место покупки:")
    bot.register_next_step_handler(msg, lambda msg: process_location_step(msg, debtor_id, amount))

def process_location_step(message, debtor_id, amount):
    location = message.text
    # Создание подключения к базе данных SQLite
    conn = sqlite3.connect('debts.db')
    c = conn.cursor()
    # Добавление долга в базу данных
    c.execute("INSERT INTO debts (debtor_id, name, amount, location) VALUES (?, '', ?, ?)", (debtor_id, amount, location))
    conn.commit()
    conn.close()
    bot.send_message(message.chat.id, f"Долг для пользователя с ID {debtor_id} успешно добавлен")

# Обработчик команды /view_debts
@bot.message_handler(commands=['view_debts'])
def view_debts(message):
    chat_id = message.chat.id
    # Создание подключения к базе данных SQLite
    conn = sqlite3.connect('debts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM debts")
    rows = c.fetchall()
    for row in rows:
        bot.send_message(chat_id, f"ID: {row[0]}, Долг для пользователя с ID {row[1]} на сумму {row[3]} рублей в месте {row[4]}")
    conn.close()

# Обработчик команды /pay_debt
@bot.message_handler(commands=['pay_debt'])
def pay_debt(message):
    chat_id = message.chat.id
    # Создание подключения к базе данных SQLite
    conn = sqlite3.connect('debts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM debts")
    rows = c.fetchall()
    if rows:
        markup = types.InlineKeyboardMarkup()
        for row in rows:
            markup.row(types.InlineKeyboardButton('Подтвердить', callback_data=f'confirm_{row[0]}'),
                       types.InlineKeyboardButton('Отклонить', callback_data=f'reject_{row[0]}'))
        bot.send_message(chat_id, "Выберите долг для оплаты:", reply_markup=markup)
    else:
        bot.reply_to(message, "У вас нет долгов")
    conn.close()

# Обработчик нажатия кнопки в инлайн-клавиатуре
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    # Создание подключения к базе данных SQLite
    conn = sqlite3.connect('debts.db')
    c = conn.cursor()
    command, debt_id = call.data.split('_')
    debt_id = int(debt_id)
    if command == 'confirm':
        c.execute("DELETE FROM debts WHERE id=?", (debt_id,))
        conn.commit()
        bot.send_message(call.message.chat.id, "Долг успешно оплачен")
    elif command == 'reject':
        bot.send_message(call.message.chat.id, "Оплата долга отклонена")
    conn.close()

# Запуск бота
bot.polling()
