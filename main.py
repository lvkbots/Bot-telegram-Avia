import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
import logging

# Configuration
TOKEN = os.environ.get('7184666905:AAFd2arfmIFZ86cp9NNVp57dKkH6hAVi4iM')
PORT = int(os.environ.get('PORT', 5000))

# Initialisation
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Bonjour. Je m'appelle Mustafa Zulu 🖥️\n\n"
        "Mon équipe a développé un algorithme pour calculer le prochain coef dans Aviator "
        "avec une précision de *99,997%* ✅\n\n"
        "Nous vous apprendrons à utiliser ce programme pour *gagner 120 000 dès aujourd'hui* 💸💰\n\n"
        "Écrivez-moi et je vous donnerai le programme 🎁"
    )
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("✅ Écrire ✉️", url="https://t.me/moustaphalux"))
    markup.add(InlineKeyboardButton("✅ Critiques 💲", url="https://t.me/moustaphalux"))
    markup.add(InlineKeyboardButton("💻 Fonctionnement du programme", url="https://t.me/moustaphalux"))
    
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

@server.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK"

@server.route('/')
def webhook_setup():
    bot.remove_webhook()
    bot.set_webhook(url=f'https://{os.environ.get("RENDER_EXTERNAL_URL")}/{TOKEN}')
    return "Webhook configuré"

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=PORT)
