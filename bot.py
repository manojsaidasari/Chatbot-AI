import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8107752141:AAGwU_0zuOmNCYzM0S68bk7v26ovqy_SCnc")

# In-memory context store (per user)
user_context = {}

# Simple Q&A knowledge base
qa_pairs = {
    'hello': 'Hi there! How can I help you today?',
    'what is your name?': 'I am your friendly chatbot!',
    'how are you?': 'I am just a bot, but I am doing great!'
}

def get_answer(question):
    # Simple Q&A lookup (case-insensitive)
    return qa_pairs.get(question.lower(), "Sorry, I don't know the answer to that yet.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your chatbot. Ask me anything!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text
    # Store last message as context (expand as needed)
    user_context[user_id] = {'last_message': text}
    answer = get_answer(text)
    await update.message.reply_text(answer)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print('Bot is running...')
    app.run_polling()

if __name__ == '__main__':
    main() 