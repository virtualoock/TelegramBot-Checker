import requests
import datetime
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a Discord token to check its validity and get additional information.')

def check_token(update: Update, context: CallbackContext) -> None:
    token = update.message.text
    discord_api_url = f"https://discord.com/api/v10/users/@me/guilds"
    
    headers = {
        "Authorization": f"Bot {token}"
    }

    response = requests.get(discord_api_url, headers=headers)

    if response.status_code == 200:
        guilds = response.json()

        if guilds:
            guild_list = "\n".join([f"{index + 1}. {guild['name']}" for index, guild in enumerate(guilds)])
            reply_text = f"Discord token is valid!\n\nJoined servers:\n{guild_list}"
            update.message.reply_text(reply_text)
        else:
            update.message.reply_text("The user is not a member of any server.")
    else:
        update.message.reply_text("Invalid Discord token.")

def text_friends(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You can text your friends in Discord directly through the Discord app or website.")

if __name__ == '__main__':
    from telegram.ext import Updater

    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_token))
    dp.add_handler(CommandHandler("text_friends", text_friends))

    updater.start_polling()
    updater.idle()
