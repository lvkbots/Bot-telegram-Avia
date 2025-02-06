import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO)

# Token Telegram
TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Configuration du bot
bot = telebot.TeleBot(TOKEN)

# Supprimer le webhook et attendre
bot.remove_webhook()
time.sleep(0.1)

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

def main():
    logging.info("Bot démarré!")
    try:
        bot.polling(none_stop=True, interval=0, timeout=30)
    except Exception as e:
        logging.error(f"Erreur lors du polling : {e}")
        time.sleep(15)
        main()

if __name__ == '__main__':
    main()
