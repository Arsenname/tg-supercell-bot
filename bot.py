from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7487056793:AAH-cRO2qJHyjQIfMwDqsNz7Rt0QF8_P0ZI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Чтобы купить Бравл Пасс, перейди по ссылке:\nhttp://127.0.0.1:5000"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()
