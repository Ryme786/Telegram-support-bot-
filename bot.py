import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Your bot's token from BotFather
TOKEN = os.environ.get('TELEGRAM_TOKEN')

# The auto-reply message
LAKSHYA_REPLY = """
Telegram private group e upload kori lecture
Pw
Soms classroom
Soe bangla
Bong mistry pabe

Price 199 rs
"""

# This function will be called when a user starts a chat with your bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am here to help with your course questions. Send "lakshya" for details.')

# This function will handle the auto-reply
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower() # Convert message to lowercase
    if 'lakshya' in user_message:
        await update.message.reply_text(LAKSHYA_REPLY)
    else:
        # You can add a default reply for other messages if you want
        await update.message.reply_text('Thank you for your message! I will get back to you soon.')
        # This is where you can also forward the message to yourself
        # Replace YOUR_TELEGRAM_USER_ID with your actual user ID
        # You can get your user ID by messaging @userinfobot on Telegram
        await context.bot.forward_message(chat_id='6705657501', from_chat_id=update.message.chat_id, message_id=update.message.message_id)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - reply to the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()
  
