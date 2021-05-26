from telegram import ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from contents.text import BuyProducts, AboutCompany, Contacts, SupportCenter, Settings
from contents.text import main_menu_markup



def main_menu(update, context: CallbackContext):
    chatId = update.effective_user.id
    buttons = [
        [BuyProducts[language(update)]],
        [AboutCompany[language(update)], Contacts[language(update)]],
        [SupportCenter[language(update)], Settings[language(update)]],
    ]
    context.bot.send_message(chat_id=chatId,
                             text=main_menu_markup[language(update)],
                             reply_markup=ReplyKeyboardMarkup(buttons,
                                                              resize_keyboard=True)
                             )


def echo_it(update, context: CallbackContext):
    update.effective_message.reply_text(update.effective_message.text)

