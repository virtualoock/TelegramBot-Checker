Start Command (/start):

This command initiates the bot and prompts the user to send a Discord token for validation.
Check Token Function (check_token):

When a user sends a Discord token, the bot sends a request to the Discord API to retrieve information about the user.
If the response status code is 200 (OK), it means the token is valid, and the script extracts user information like ID, username, and account creation date.
The script then sends a reply to the user on Telegram, including the user information.
If the user is a member of any Discord servers, it lists the server names.
Text Friends Command (/text_friends):

This command informs the user that they can text their friends in Discord directly through the Discord app or website.
Note: Discord bots do not have the capability to send direct messages between users, so users are encouraged to use the official Discord platform for private messaging.
Telegram Bot Setup:

The script sets up the Telegram bot using the python-telegram-bot library.
It uses the Updater class to handle updates from Telegram.
Running the Bot:

The script starts polling for updates, allowing the bot to respond to commands and messages on Telegram.
Please note that while the script checks the validity of Discord tokens and provides some user information, it does not have the ability to send direct messages to friends on Discord due to limitations imposed by the Discord API. Users are advised to use the official Discord platform for private messaging.

This is a beta and it is possible that the code will not work, if you change the code, please mention me and I will try to add new functions.

Version 2 Changes:
New Function get_user_avatar:

This function allows users to retrieve and view their Discord avatar.
Users can trigger this function using the "/get_user_avatar" command in the Telegram chat.
The function sends the user's Discord avatar as a photo to the Telegram user.
Argument Handling in get_user_avatar:

The function uses pass_args=True in the CommandHandler to handle arguments passed with the command.
If the user includes a Discord token as an argument after the "/get_user_avatar" command, the function uses that token. Otherwise, it uses the message text as the token.
Update in MessageHandler for check_token:

I adjusted the check_token function to handle tokens passed as arguments in a more consistent way.
