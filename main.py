from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from contents.text import *
from AuthConfigs.keys import API_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


image = open("assets/brand.png", 'rb')

def start_command(update, context):
    message = update.message
    buttons = [
        [InlineKeyboardButton(ButtonUzbek, callback_data='uz'),
         InlineKeyboardButton(ButtonRussian, callback_data='ru'),
         InlineKeyboardButton(ButtonEnglish, callback_data='en')]
    ]
    context.bot.send_message(chat_id=message.chat_id,
                             reply_markup=InlineKeyboardMarkup(buttons),
                             text=choose_language)

def button(update: Update, _: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.delete_message()

    query.bot.send_photo(chat_id=query.message.chat.id,
                         photo="AgACAgIAAxkDAAMIYKgNC14qhXiIsOFWnCIW1ZD3Ys0AAom3MRvc2kBJVRYbgPN4eYshICKbLgADAQADAgADbQADdm4GAAEfBA",
                         caption=greeting_text[query['data']],)


def main():
    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()

    updater.idle()
