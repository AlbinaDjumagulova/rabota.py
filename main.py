import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6493686163:AAEbX3jfHwdzbSYAW02JGlFxV8bcZR2HkaE')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nкак дела?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Хорошо сама как ', callback_data='Good. What about you')
    markup.add(button_yes)
    button_no = types.InlineKeyboardButton(text=' Нет не очень', callback_data='no')
    markup.add(button_no)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "Хорошо сама как":
            second_mess = "У меня все хорошо 👌Я учусь на программиста и советую этот сайт,😉"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Нажми", url="https://www.instagram.com"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)





botTimeWeb.infinity_polling()
