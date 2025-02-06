import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request

# Configuration
TOKEN = 'YOUR_BOT_TOKEN'  # Remplacez par votre token réel
PORT = int(os.environ.get('PORT', 5000))

# Initialisation
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Création des boutons avec des liens
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("📞 Contact", url="https://t.me/moustaphalux"),
        InlineKeyboardButton("📊 Statistiques", url="https://t.me/moustaphalux")
    )
    markup.row(
        InlineKeyboardButton("💡 Programme", url="https://t.me/moustaphalux")
    )

    # Message de bienvenue
    welcome_message = (
        "🚀 *Algorithme Aviator* 🎲\n\n"
        "Précision : *99,997%*\n"
        "Gain potentiel : *120 000*\n\n"
        "Cliquez sur les boutons pour plus d'informations !"
    )

    # Envoi du message de bienvenue avec les boutons
    bot.send_message(
        message.chat.id, 
        welcome_message, 
        parse_mode="Markdown", 
        reply_markup=markup
    )

# Webhook pour recevoir les mises à jour du bot
@server.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK"

# Configuration du webhook
@server.route('/')
def webhook_setup():
    bot.remove_webhook()
    bot.set_webhook(url=f'https://{os.environ.get("RENDER_EXTERNAL_URL")}/{TOKEN}')
    return "Webhook configuré"

# Exécution du serveur Flask
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=PORT)
