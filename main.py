import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await context.bot.send_message(chat_id=OWNER_ID, text=f"❓ Новый анонимный вопрос:\n\n{update.message.text}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))

if __name__ == '__main__':
    print("Бот запущен...")
    app.run_polling()
