from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

TOKEN = "8755091810:AAEn5lACr6TWIYtZHgPh-SXCMgTUIoy_G_g"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я бот 🤖\nНапиши мені щось, і я відповім."
    )


async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if "привіт" in user_text:
        response = "Привіт 😊 Як справи?"
    elif "як справи" in user_text:
        response = "У мене все чудово 😄 А у тебе?"
    elif "тебе звати" in user_text:
        response = "Я Telegram-бот на Python 🤖"
    else:
        response = f"Ти написав: {update.message.text}"

    await update.message.reply_text(response)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

app.run_polling()
