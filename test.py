from telegram import Update, Poll
from telegram.ext import Application, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Напиши /game чтобы создать опрос")

async def game(update: Update, context: CallbackContext):
    question = "Когда играть? "
    options = ["18:00", "18:30", "19:00", "19:30", "никаких игров"]

    await context.bot.send_poll(
        chat_id=update.message.chat_id,
        question=question,
        options=options,
        is_anonymous=False, 
        allows_multiple_answers=True,
    )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("game", game))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
