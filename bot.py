from telegram.ext import Updater, CommandHandler

# توکن رباتت رو اینجا بذار
TOKEN = "YOUR_BOT_TOKEN_HERE"

def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"سلام {user.first_name}! به ربات من خوش اومدی! 😊")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()from telegram.ext import Updater, CommandHandler

# توکن رباتت رو اینجا بذار
TOKEN =7990684653:"AAGFS1L4mi2jcdGqAeaVaZ7qZMgBVnfchFk"

def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"سلام {user.first_name}! به ربات من خوش اومدی! 😊")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
