import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "9263178961:AAFN1YbgL4bg75HA78_CcR-ZyklZ227dsfE"

GEMINI_API_KEY = "AQ.Ab8RN6IsRm6KgSnDJ2hhHw4g3R0TKYknLOWyAJOfmGolrU-C8Q"

MY_TELEGRAM_ID = 6109318639

bot = telebot.TeleBot("9263178961:AAFN1YbgL4bg75HA78_CcR-ZyklZ227dsfE")

genai.configure(api_key=AQ.Ab8RN6IsRm6KgSnDJ2hhHw4g3R0TKYknLOWyAJOfmGolrU-C8Q)
model = genai.GenerativeModel("gemini-1.5-flash")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.id != MY_TELEGRAM_ID:
        bot.reply_to(message, "Этот бот создан только для личного использования.")
        return
    
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

print("Бот успешно запущен и ждет сообщения!")
bot.infinity_polling()
