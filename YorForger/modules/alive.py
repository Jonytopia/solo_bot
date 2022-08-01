from YorForger import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.utils.helpers import escape_markdown

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/99829b67f239007a33287.jpg"


def alive(update: Update, context: CallbackContext):
    TEXT = "Hi **{}**[,](https://telegra.ph/file/4d8263c4c00626572f048.jpg) I Am **solo¥**!\n\n◈I'm working properly! \n\n◈My MASTER - **[jonytopia ](https://t.me/dark_x_star)**\n\n◈Thanks For Using Me Here◈"

    first_name = update.effective_user.first_name

    update.effective_message.reply_text(
        TEXT.format(escape_markdown(first_name)), 
        parse_mode=ParseMode.MARKDOWN,
    )

void_handler = CommandHandler("alive", alive, run_async = True)
dispatcher.add_handler(void_handler)


__help__ = """ 
❂ /alive: To check if bot is alive or not."""
   
__mod_name__ = "Alive"
