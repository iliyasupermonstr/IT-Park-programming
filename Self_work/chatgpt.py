import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

# Токены доступа к API
TELEGRAM_TOKEN = '6858600007:AAEtdYrEDVDu2wGpm7E0NHMq_Si-Bhh9MYM'
OPENAI_API_KEY = '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'

# Инициализация клиента Telegram Bot API и OpenAI API
bot = telegram.Bot(token=TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Я бот с ChatGPT. Просто напиши мне что-нибудь, и я постараюсь ответить.")

# Обработчик текстовых сообщений
def handle_message(update, context):
    message_text = update.message.text
    response = generate_response(message_text)
    update.message.reply_text(response)

# Генерация ответа с помощью ChatGPT
def generate_response(input_text):
    prompt = f"Conversation:\nUser: {input_text}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    return response.choices[0].text.strip()

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
