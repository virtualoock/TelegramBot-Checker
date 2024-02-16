
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





Version 3 Changes:
New Function get_user_activity:

This function retrieves and displays information about the user's recent activity on Discord.
It includes details such as the account creation date and the last time the user was online.
Users can trigger this function using the "/get_user_activity" command in the Telegram chat.
CommandHandler for get_user_activity:

I added a new CommandHandler for the "/get_user_activity" command, linking it to the get_user_activity function



Version 4 Changes:
Inline Keyboard Buttons:

I added inline keyboard buttons for each command to improve user interaction.
Users can now tap on buttons instead of typing commands manually.
Modified Command Handling:

The get_user_activity function now handles both inline button presses and command input.
