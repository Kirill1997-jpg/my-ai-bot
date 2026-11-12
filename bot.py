import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "ВАШ_ТОКЕН_ИЗ_BOTFATHER"

GEMINI_API_KEY = "AQ.Ab8RN6Kdw1gt4HaticSvSpBETu0ykb6thJJhDAH7F8JjGOPoLw"

MY_TELEGRAM_ID = 6109318639

bot = telebot.TeleBot(9263178961:AAFN1YbgL4bg75HA78_CcR-ZyklZ227dsfE)
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != MY_TELEGRAM_ID:
        return
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

bot.infinity_polling()
