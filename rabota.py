import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6466214978:AAHMEXSk3YTh1bUQTTInbq6YgMrKjQK4dvQ')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, Здраствуйте!\nЯ не давно открыла магазин одежды, В чес открытия у нас идет акция 50% ?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    markup.add(button_yes)
    button_no = types.InlineKeyboardButton(text='Адрес ', callback_data='no')
    markup.add(button_no)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "Переходите по ссылку но пока там нечего нет"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Нажми👆🏻", url="https://www.instagram.com"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'Адрес':
            second_mess = "Да кнш!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Можешь нажать", url="Улица ленина 351"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)




botTimeWeb.infinity_polling()
