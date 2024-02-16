import requests
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a Discord token to check its validity and get additional information.')

def check_token(update: Update, context: CallbackContext) -> None:
    token = update.message.text
    user_info_url = "https://discord.com/api/v10/users/@me"
    guilds_url = "https://discord.com/api/v10/users/@me/guilds"
    
    headers = {
        "Authorization": f"Bot {token}"
    }

    # Get user information
    user_response = requests.get(user_info_url, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()
        username = user_data.get("username")
        discriminator = user_data.get("discriminator")
        user_id = user_data.get("id")

        # Get guilds the user is a member of
        guilds_response = requests.get(guilds_url, headers=headers)
        guilds = guilds_response.json()

        if guilds:
            guild_list = "\n".join([f"{index + 1}. {guild['name']}" for index, guild in enumerate(guilds)])
            reply_text = f"Discord token is valid!\n\nUser ID: {user_id}\nUsername: {username}#{discriminator}\nJoined servers:\n{guild_list}"
            update.message.reply_text(reply_text)
        else:
            update.message.reply_text("The user is not a member of any server.")
    else:
        update.message.reply_text("Invalid Discord token.")

def text_friends(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You can text your friends in Discord directly through the Discord app or website.")

def get_user_info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This function will display additional user information from the Discord API.")

def get_user_avatar(update: Update, context: CallbackContext) -> None:
    token = context.args[0] if context.args else update.message.text

    user_info_url = "https://discord.com/api/v10/users/@me"
    avatar_url = "https://discord.com/api/v10/users/@me/avatar"

    headers = {
        "Authorization": f"Bot {token}"
    }

    # Get user avatar
    avatar_response = requests.get(avatar_url, headers=headers)

    if avatar_response.status_code == 200:
        # Send the avatar as a photo to the Telegram user
        update.message.reply_photo(avatar_response.content)
    else:
        update.message.reply_text("Unable to retrieve the user's avatar.")

def get_user_activity(update: Update, context: CallbackContext) -> None:
    token = context.args[0] if context.args else update.message.text
    user_info_url = "https://discord.com/api/v10/users/@me"

    headers = {
        "Authorization": f"Bot {token}"
    }

    # Get user information
    user_response = requests.get(user_info_url, headers=headers)

    if user_response.status_code == 200:
        user_data = user_response.json()
        account_creation_date = user_data.get("created_at")
        last_online = user_data.get("last_message_id")

        reply_text = f"Account Creation Date: {account_creation_date}\nLast Online: {last_online}"
        update.message.reply_text(reply_text)
    else:
        update.message.reply_text("Unable to retrieve user activity information.")

if __name__ == '__main__':
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_token))
    dp.add_handler(CommandHandler("text_friends", text_friends))
    dp.add_handler(CommandHandler("get_user_info", get_user_info))
    dp.add_handler(CommandHandler("get_user_avatar", get_user_avatar, pass_args=True))
    dp.add_handler(CommandHandler("get_user_activity", get_user_activity, pass_args=True))

    updater.start_polling()
    updater.idle()
