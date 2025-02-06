import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

# Configuration
TOKEN = '7184666905:AAFd2arfmIFZ86cp9NNVp57dKkH6hAVi4iM'
PORT = int(os.environ.get('PORT', 5000))

# Initialisation
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("📞 Contact", url="https://t.me/moustaphalux"),
        InlineKeyboardButton("📊 Statistiques", url="https://t.me/moustaphalux")
    )
    markup.row(
        InlineKeyboardButton("💡 Programme", url="https://t.me/moustaphalux")
    )

    welcome_message = (
        "🚀 *Algorithme Aviator* 🎲\n\n"
        "Précision : *99,997%*\n"
        "Gain potentiel : *120 000*\n\n"
        "Cliquez sur les boutons pour plus d'informations !"
    )

    bot.send_message(
        message.chat.id, 
        welcome_message, 
        parse_mode="Markdown", 
        reply_markup=markup
    )

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
