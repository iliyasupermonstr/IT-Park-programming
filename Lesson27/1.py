import webbrowser
import telebot
from telebot import types
import sqlite3
import requests
import json

API = '98ca66e03000af47ee02eb13bf21076f'

bot = telebot.TeleBot('6822383921:AAHgv1KZaGDE1p1jOF3gCmDHiAocsboagsM')

@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(message.chat.id,"Рад тебя видеть, введи пожалуйста свой город.")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Температура на улице: {data["main"]["temp"]}')

        if temp > 5.0:
            image = "skc_dc.png"
        elif temp < -10.0:
            image = "snow.png"
        else:
            image = "ovc.png"
        file = open('./' + image , 'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message,"Город указан неверно")
bot.polling(none_stop=True,interval=0)