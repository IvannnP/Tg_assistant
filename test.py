import telebot
from collections import defaultdict
from telebot import types

bot = telebot.TeleBot('5017039715:AAGh0JDG-nx12I3Jx4rpJgZeFvfkCzflVfE')

users_start = [7422870]  # chat id

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

    item1 = types.KeyboardButton('Математеический Анализ')


    markup.add(item1)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup = markup)


@bot.message_handler(func=lambda message: message.chat.id not in users_start, commands=['redactor_mode'])
def not_admin(message):
    bot.send_message(message.chat.id, 'У Вас нет прав на выполнение данной команды')

@bot.message_handler(func=lambda message: True , commands=['redactor_mode'])
def admin(message):
    bot.send_message(message.chat.id, 'У вас есть доступ')
    msgPrice = bot.send_message(message.chat.id, 'Set your price:')
    bot.register_next_step_handler(msgPrice , step_Set_Price)

def step_Set_Price(message):
        userPrice= message.text

        @bot.message_handler(content_types=['text'])
        def bot_message(message):
            if message.chat.type == 'private':
                if message.text == 'Математеический Анализ':
                    bot.send_message(message.chat.id, userPrice)



    # RUN








bot.polling(none_stop=True)

