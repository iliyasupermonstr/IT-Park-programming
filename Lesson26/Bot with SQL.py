import webbrowser
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6822383921:AAHgv1KZaGDE1p1jOF3gCmDHiAocsboagsM')
@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id,"Рад тебя видеть, введи пожалуйста свой город.")

# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('for_bot.sql')
#     cur = conn.cursor()

#     cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), pass VARCHAR(50))')
#     conn.commit()
#     cur.close()
#     conn.close()

#     bot.send_message(message.chat.id, 'Привет, сейчас я тебя зарегистрирую! Введи свое имя!')
#     bot.register_next_step_handler(message, user_name)

# def user_name(message):
#     global name
#     name = message.text.strip()  
#     bot.send_message(message.chat.id, 'Введите пароль')
#     bot.register_next_step_handler(message, user_pass) 

# def user_pass(message):
#     password = message.text.strip()  

#     conn = sqlite3.connect('for_bot.sql')
#     cur = conn.cursor()

#     cur.execute(f"INSERT INTO users (name, pass) VALUES ('%s', '%s' )" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()

#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
#     bot.send_message(message.chat.id, 'Пользователь зарегестрирован!', reply_markup=markup)

# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):
#     conn = sqlite3.connect("for_bot.sql")
#     cur = conn.cursor()

#     cur.execute('SELECT * FROM users')
#     users = cur.fetchall()
#     info = ''

#     for el in users:
#         info += f'Имя {el[1]}, пароль: {el[2]}\n'

#     cur.close()
#     conn.close()
        
#     bot.send_message(call.message.chat.id,info)

bot.polling(none_stop=True, interval=0)