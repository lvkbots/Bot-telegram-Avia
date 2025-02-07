# render.yaml
services:
  - type: web
    name: telegram-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py

# requirements.txt
python-telegram-bot==20.7
python-dotenv==1.0.0
Flask==2.0.1

# main.py
import os
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration Flask
app = Flask(__name__)

# Configuration Telegram
TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📸 Photos", callback_data='photo'),
            InlineKeyboardButton("ℹ️ Info", callback_data='about')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Bienvenue! Je suis votre assistant bot.",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'photo':
        await query.message.reply_text("Voici votre photo!")
    elif query.data == 'about':
        await query.message.reply_text("Je suis un bot créé pour vous servir!")

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    application.run_polling()

@app.route('/')
def home():
    return 'Bot is running!'

if __name__ == '__main__':
    # Démarrage du bot en arrière-plan
    import threading
    bot_thread = threading.Thread(target=main)
    bot_thread.start()
    
    # Démarrage du serveur Flask
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
