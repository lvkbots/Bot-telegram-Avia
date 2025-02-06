# main.py
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Bonjour. Je m'appelle Mustafa Zulu 🖥️\n\n"
         "Mon équipe et moi-même avons développé un algorithme de programme qui calcule le prochain coef dans le jeu Aviator "
         "avec une précision de *99,997%* ✅\n\n"
         "Nous vous apprendrons à utiliser ce programme pour *gagner 120 000 dès aujourd'hui* 💸💰\n\n"
         "Écrivez-moi et je vous donnerai le programme 🎁"
    )
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ Écrire ✉️", url="https://t.me/moustaphalux"))
    markup.add(InlineKeyboardButton("✅ Critiques 💲", url="https://t.me/moustaphalux"))
    markup.add(InlineKeyboardButton("💻 Fonctionnement du programme", url="https://t.me/moustaphalux"))
    
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

print("Bot démarré!")
bot.polling(none_stop=True)
