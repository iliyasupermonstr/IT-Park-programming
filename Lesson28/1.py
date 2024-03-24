
import telebot
from telebot import types
import sqlite3
from currency_converter import CurrencyConverter

bot = telebot.TeleBot('6822383921:AAHgv1KZaGDE1p1jOF3gCmDHiAocsboagsM')

currency = CurrencyConverter()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму:')
    bot.register_next_step_handler(message,summa)

def summa(message):
    global amount
    amount = message.text.strip()
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id,'Неверный формат. Нужно вводить сумму')
        bot.register_next_step_handler(message,summa)
        return

    if amount > 0:

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id,'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,"Число должно быть больше 0")
        bot.register_next_step_handler(message,summa)

@bot.callback_query_handler(func = lambda call:True)
def callback(call):
    if call.data != 'else':

        values = call.data.upper().split('/')
        res = currency.convert(amount,values[0],values[1])
        bot.send_message(call.message.chat.id, f'Результат: {round(res,2)}. Можете вводить дальше')
        bot.register_next_step_handler(call.message,summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите валюты через "/"')
        bot.register_next_step_handler(call.message,my_currency)
def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount,values[0],values[1])
        bot.send_message(message.chat.id, f'Результат: {round(res,2)}. Можете вводить дальше')
        bot.register_next_step_handler(message,summa)
    except Exception as e:
        bot.send_message(message.chat.id,'Что то пошло не так , введите значение заново:')
        bot.register_next_step_handler(message,my_currency)

bot.polling(none_stop=True,interval=0)