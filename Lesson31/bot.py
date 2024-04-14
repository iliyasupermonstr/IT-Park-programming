import json
import time
import telebot
import requests
import base64

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('6858600007:AAEtdYrEDVDu2wGpm7E0NHMq_Si-Bhh9MYM')
class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024,style=3):
        styles = ["KANDINSKY","UHD","ANIME","DEFAULT"]
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "style": styles[style],
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id," Привет! Что вы хотите сгенерировать?")

@bot.message_handler(func=lambda message: True)
def generate_buttons(message):
    keyboard = ReplyKeyboardMarkup(row_width=4)
    keyboard.add(KeyboardButton('KANDINSKY'))
    keyboard.add(KeyboardButton('UHD'))
    keyboard.add(KeyboardButton('ANIME'))
    keyboard.add(KeyboardButton('DEFAULT'))
    msg = bot.send_message(message.chat.id,"выберите стиль рисовки", reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_style_choice, message)

def process_style_choice(message,original_message):
    chosen_style = message.text
    style_id = 3
    if chosen_style == 'KANDINSKY':
        style_id = 0
    if chosen_style == 'UHD':
        style_id = 1
    if chosen_style == 'ANIME':
        style_id = 2
    if chosen_style == 'DEFAULT':
        style_id = 3

    generate_image(style_id, original_message)
@bot.message_handler(func=lambda message:True)
def generate_image(message):

    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'B2BE478A66E25C0DBA889A201BDCC4FD', '40C583D871D33B629236AE07A516EE7B')
    model_id = api.get_model()
    uuid = api.generate(message.text, model_id,style=2)
    images = api.check_generation(uuid)
    image_base64 = images[0]
    image_data = base64.b64decode(image_base64)
    bot.send_photo(message.chat.id, image_data,caption="Изображение по вашему вопросу")
bot.polling()


#Не забудьте указать именно ваш YOUR_KEY и YOUR_SECRET