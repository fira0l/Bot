import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("token")
WEB_APP_URL = "https://telegrambot-48lt.onrender.com"
PORT = 8000;

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            text="💼 View Portfolio & Hire Me",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hey there! Check out my portfolio and feel free to order a design job. 👇",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")  # optional log
    app.run_polling()
