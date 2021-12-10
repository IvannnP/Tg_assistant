import telebot
from collections import defaultdict
from telebot import types

bot = telebot.TeleBot('5017039715:AAGh0JDG-nx12I3Jx4rpJgZeFvfkCzflVfE')

users_start = [742287025]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

    item1 = types.KeyboardButton('Математеический Анализ')
    item2 = types.KeyboardButton('Линейная Алгебра')
    item3 = types.KeyboardButton('Дискретная Математика')
    item4 = types.KeyboardButton('Микроэкономика')
    item5 = types.KeyboardButton('Введение в бизнес-информатику')

    markup.add(item5, item4, item3, item2, item1)


    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markup)



@bot.message_handler(func=lambda message: message.chat.id not in users_start, commands=['redactor_mode'])
def not_admin(message):
                bot.send_message(message.chat.id, 'У Вас нет прав на выполнение данной команды')

@bot.message_handler(func=lambda message: True, commands=['redactor_mode'])
def step0(message):
                bot.send_message(message.chat.id, 'У вас есть доступ')


                menu0 = telebot.types.InlineKeyboardMarkup()
                menu0.add(telebot.types.InlineKeyboardButton(text='Математеический Анализ', callback_data='sub1'))
                menu0.add(telebot.types.InlineKeyboardButton(text='Линейная Алгебра', callback_data='sub2'))
                menu0.add(telebot.types.InlineKeyboardButton(text='Дискретная Математика', callback_data='sub3'))
                menu0.add(telebot.types.InlineKeyboardButton(text='Микроэкономика', callback_data='sub4'))
                menu0.add(telebot.types.InlineKeyboardButton(text='Введение в бизнес-информатику', callback_data='sub5'))

                bot.send_message(message.chat.id, text='Выберите предмет', reply_markup=menu0)

                @bot.callback_query_handler(func=lambda call: True)
                def step(call):
                    if call.data == 'sub1':


                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week11'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week12'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week13'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week14'))

                        bot.send_message(message.chat.id, text='Окей, выберите дату', reply_markup=menu1)


                        if call.data == 'week11':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')

                        elif call.data == 'week12':
                                    bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week13':
                                    bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week14':
                                    bot.send_message(message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub2':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week21'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week22'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week23'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week24'))

                        bot.send_message(message.chat.id, text='Окей, выберите дату', reply_markup=menu1)

                        if call.data == 'week21':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week22':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week23':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week24':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub3':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week31'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week32'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week33'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week34'))

                        bot.send_message(message.chat.id, text='Окей, выберите дату', reply_markup=menu1)

                        if call.data == 'week31':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week32':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week33':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week34':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub4':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week41'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week42'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week43'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week44'))

                        bot.send_message(message.chat.id, text='Окей, выберите дату', reply_markup=menu1)

                        if call.data == 'week41':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week42':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week43':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week44':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub5':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week1'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week2'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week3'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week4'))

                        bot.send_message(message.chat.id, text='Окей, выберите дату', reply_markup=menu1)

                        if call.data == 'week51':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')

                        elif call.data == 'week52':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week53':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')
                        elif call.data == 'week54':
                            bot.send_message(message.chat.id, text='Отравьте новое задание')





@bot.message_handler(content_types=['text'])
def bot_message(message):
        if message.chat.type == 'private':
            if message.text == 'Математеический Анализ':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week011'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week012'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week013'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week014'))

                bot.send_message(message.chat.id, text='Выберите дату,текущего месяца', reply_markup=menu1)



            if message.text == 'Линейная Алгебра':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week021'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week022'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week023'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week024'))

                bot.send_message(message.chat.id, text='Выберите дату,текущего месяца', reply_markup=menu1)



            if message.text == 'Дискретная Математика':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week031'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week032'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week033'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week034'))

                bot.send_message(message.chat.id, text='Выберите дату,текущего месяца', reply_markup=menu1)



            if message.text == 'Микроэкономика':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week041'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week042'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week043'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week044'))

                bot.send_message(message.chat.id, text='Выберите дату,текущего месяца', reply_markup=menu1)



            if message.text == 'Введение в бизнес-информатику':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week051'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week052'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week053'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week054'))

                bot.send_message(message.chat.id, text='Выберите дату,текущего месяца', reply_markup=menu1)

                @bot.callback_query_handler(func=lambda call: True)
                def step1(call):
                    if call.data == 'week011':
                            bot.send_message(message.chat.id, text='Задание')
                    elif call.data == 'week012':
                            bot.send_message(message.chat.id, text='задание')
                    elif call.data == 'week013':
                            bot.send_message(message.chat.id, text='О задание')
                    elif call.data == 'week014':
                            bot.send_message(message.chat.id, text='задание')

                    if call.data == 'week021':
                        bot.send_message(message.chat.id, text='Задание')
                    elif call.data == 'week022':
                        bot.send_message(message.chat.id, text='задание')
                    elif call.data == 'week023':
                        bot.send_message(message.chat.id, text='О задание')
                    elif call.data == 'week024':
                        bot.send_message(message.chat.id, text='задание')

                    if call.data == 'week031':
                        bot.send_message(message.chat.id, text='Задание')
                    elif call.data == 'week032':
                        bot.send_message(message.chat.id, text='задание')
                    elif call.data == 'week033':
                        bot.send_message(message.chat.id, text='О задание')
                    elif call.data == 'week034':
                        bot.send_message(message.chat.id, text='задание')

                    if call.data == 'week041':
                        bot.send_message(message.chat.id, text='Задание')
                    elif call.data == 'week042':
                        bot.send_message(message.chat.id, text='задание')
                    elif call.data == 'week043':
                        bot.send_message(message.chat.id, text='О задание')
                    elif call.data == 'week044':
                        bot.send_message(message.chat.id, text='задание')




                    if call.data == 'week051':
                        bot.send_message(message.chat.id, text='Задание')
                    elif call.data == 'week052':
                        bot.send_message(message.chat.id, text='задание')
                    elif call.data == 'week053':
                        bot.send_message(message.chat.id, text='О задание')
                    elif call.data == 'week054':
                        bot.send_message(message.chat.id, text='задание')

















bot.polling(none_stop=True)

