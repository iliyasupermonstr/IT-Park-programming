import webbrowser
import telebot
from telebot import types
bot = telebot.TeleBot('6822383921:AAHgv1KZaGDE1p1jOF3gCmDHiAocsboagsM')

name = ''
surname = ''
age = 0

@bot.message_handler(content_types=['name'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')
    
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет тебя зовут '+name+' '+surname+'?')  
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text = "Да",callback_data = "yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text = "Нет",callback_data = "no")
    keyboard.add(key_no)
    question = "Тебе "+str(age)+" лет тебя зовут "+name+" "+surname+" ?"
    bot.send_message(message.from_user.id,text = question,reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Запомню: )')
@bot.message_handler(commands = ["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn = types.KeyboardButton("Перейти на сайт")
    markup.row(btn)
    btn2 = types.KeyboardButton("Удалить фото")
    btn3 = types.KeyboardButton("Изменить  текст")
    markup.row(btn2,btn3)
    file = open("C7E76371-45F4-42DE-B5DB-18FD55DB5638_1_105_c.jpeg","rb")
    bot.send_photo(message.chat.id,file,reply_markup=markup)
    bot.send_message(message.chat.id,"Привет", reply_markup=markup)
    bot.register_next_step_handler(message,on_click)

def on_click(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id,"website is open")
    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id,"Deleted")
    elif message.text == "Изменить текст":
        bot.send_message(message.chat.id,)

# @bot.message_handler(commands = ["site","website"])
# def site(message):
#     webbrowser.open("https://www.youtube.com/watch?v=G6O_GVCRIYk")
# @bot.message_handler(content_types=  ["photo"])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton("Перейти на сайт",url = "https://www.youtube.com/watch?v=rYmWbXZB564")
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton("Удалить фото",callback_data = 'delete')
#     btn3 = types.InlineKeyboardButton("Изменить",callback_data = "edit")
#     markup.row(btn2,btn3)
#     bot.reply_to(message,"Какое красивое фото!!!!!",reply_markup = markup)
# @bot.callback_query_handler(func=lambda callback : True)
# def callback_message(callback):
#     if callback.data == "delete":
#         bot.delete_message(callback.message.chat.id,callback.message.message_id-1)
#     elif callback.data == "edit":
#         bot.edit_message_text("Edit text",callback.message.chat.id,callback.message.message_id-1)

bot.polling(none_stop=True,interval = 0)