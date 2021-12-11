import telebot
from collections import defaultdict
from telebot import types

bot = telebot.TeleBot('5039226372:AAFMQthFKe0kBDieulSYgU8ElMSnc0DiKZ0')

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

@bot.message_handler(commands=['offer'])
def offer(message):
                bot.send_message(message.chat.id, 'https://docs.google.com/document/d/1sCFEOdPUJ8nYUaAwCFf7Jcv1iJ4kYGcZsrRITx-veww/edit?usp=sharing')

@bot.message_handler(commands=['pdp'])
def pdp(message):
                bot.send_message(message.chat.id, 'https://docs.google.com/document/d/1yy5k-j_cJ5419QRJxZHLSZlO2uyZ4e7MGlNfuEzlKnI/edit?usp=sharing')

@bot.message_handler(commands=['lecturers'])
def lecturers(message):
    menu = telebot.types.InlineKeyboardMarkup()
    menu.add(telebot.types.InlineKeyboardButton(text='Математеический Aнализ', callback_data='sub01'))
    menu.add(telebot.types.InlineKeyboardButton(text='Линейная Aлгебра', callback_data='sub02'))
    menu.add(telebot.types.InlineKeyboardButton(text='Дискретная Математика', callback_data='sub03'))
    menu.add(telebot.types.InlineKeyboardButton(text='Микроэкономика', callback_data='sub04'))
    menu.add(telebot.types.InlineKeyboardButton(text='Введение в бизнес-информатику', callback_data='sub05'))

    bot.send_message(message.chat.id, text='Выберите предмет', reply_markup=menu)


@bot.message_handler(func=lambda message: True, commands=['stoffice'])
def pdp(message):
                bot.send_message(message.chat.id, 'Учебный оффис')
                bot.send_message(message.chat.id, 'Чирко Елена Александровна')
                bot.send_message(message.chat.id, 'echirko@hse.ru')
                bot.send_message(message.chat.id, '+7 (495) 772-95-90 * 28464')
                bot.send_message(message.chat.id, 'Гусева Мария Григорьевна')
                bot.send_message(message.chat.id, 'mgguseva@hse.ru')
                bot.send_message(message.chat.id, '+7 (495) 772-95-90 * 28314')


@bot.message_handler(func=lambda message: True, commands=['seminars'])
def pdp(message):
    menu = telebot.types.InlineKeyboardMarkup()

    menu.add(telebot.types.InlineKeyboardButton(text='Линейная Aлгебра', callback_data='sub12'))
    menu.add(telebot.types.InlineKeyboardButton(text='Дискретная Математика', callback_data='sub13'))


    bot.send_message(message.chat.id, text='Выберите предмет', reply_markup=menu)


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



@bot.message_handler(content_types=['text'])
def bot_message(message):
        if message.chat.type == 'private':
            if message.text == 'Математеический Анализ':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week011'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week012'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week013'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week014'))

                bot.send_message(message.chat.id, text='Выберите учебный период текущего месяца', reply_markup=menu1)



            if message.text == 'Линейная Алгебра':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week021'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week022'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week023'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week024'))

                bot.send_message(message.chat.id, text='Выберите учебный период текущего месяца', reply_markup=menu1)



            if message.text == 'Дискретная Математика':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week031'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week032'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week033'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week034'))

                bot.send_message(message.chat.id, text='Выберите учебный период текущего месяца', reply_markup=menu1)



            if message.text == 'Микроэкономика':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week041'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week042'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week043'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week044'))

                bot.send_message(message.chat.id, text='Выберите учебный период текущего месяца', reply_markup=menu1)



            if message.text == 'Введение в бизнес-информатику':
                menu1 = telebot.types.InlineKeyboardMarkup()
                menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week051'))
                menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week052'))
                menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week053'))
                menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week054'))

                bot.send_message(message.chat.id, text='Выберите учебный период текущего месяца', reply_markup=menu1)

        @bot.callback_query_handler(func=lambda call: True)
        def step1(call):

            #Математический анализ
                    if call.data == 'week011':
                            bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 1 по 5 число')
                            bot.send_message(call.message.chat.id, text='Тема "Формула Тейлора" (старый номер 10).')
                            bot.send_message(call.message.chat.id, text='Тема 10: 15.4, 17, 1.4, 1.6, 1.8, 3.10, 3.12, 3.13, 4.5, 4.6, 4.7, 4.8, 5.4, 5.6, 6, 7.4, 11.Б, 12.Б.')
                            bot.send_message(call.message.chat.id, text='Указание: рекомендуется решать задачи в указанном порядке. Обратите внимание, что в задачах 5.4, 5.6, 6 нужно получить не одну, а две интервальные оценки - одну с помощью первого (линейного) приближения, а вторую - с помощью второго (квадратичного).')
                    elif call.data == 'week012':
                          bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 6 по 12 число')
                          bot.send_message(call.message.chat.id, text='Уважаемые студенты, высылаю задание для самостоятельной работы после семинара 12.')
                          bot.send_message(call.message.chat.id, text='Тема "Графики 2, асимптоты" (старый номер 12).')
                          bot.send_message(call.message.chat.id, text='Тема 12: решить задачи 2.4, 3.6, 4.6-7, 6.1, 6.5-7, 7.7-8, 8.4-6, 9.3-4. Указание: кроме наклонных асимптот в каждой задаче также обязательно надо найти и вертикальные асимптоты или показать, что их нет.')
                    elif call.data == 'week013':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на чиле')
                    elif call.data == 'week014':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='кайфуем')


            #Линейная алгебра


                    elif call.data == 'week021':
                        bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 1 по 5 число')
                        bot.send_message(call.message.chat.id, text='Дорогие студенты, Домашнее задание на завтрашний семинар:4.62, 65, 71, 73, 79, Проскуряков 1366, 1372')
                        bot.send_message(call.message.chat.id, text='Записи сегодняшних семинаров: группа 211 https://youtu.be/tavIWHx8lSY , группа 212 https://youtu.be/_6tqS1M8yUg')
                    elif call.data == 'week022':
                        bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 6 по 12 число')
                        bot.send_message(call.message.chat.id,
                                         text='Дорогие студенты, Домашнее задание на следующий семинар: Проскуряков 1367, Ефимов Демидович 4.186, 213, 216')
                        bot.send_message(call.message.chat.id,
                                         text='Записи сегодняшних семинаров: группа 211 https://youtu.be/BJqWFKwjWzo , группа 212 https://youtu.be/7inynXtwBJE')
                    elif call.data == 'week023':

                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на чиле')
                    elif call.data == 'week024':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='кайфуем')

            #Дискретная матемтаика
                    elif call.data == 'week031':
                        bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 1 по 5 число')
                        bot.send_message(call.message.chat.id, text='Домашнее задание 288, 292, 296, 283, 271.')
                    elif call.data == 'week032':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='кайфуем')
                    elif call.data == 'week033':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на расслабоне')
                    elif call.data == 'week034':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на чиле')
            #Микроэконмика
                    elif call.data == 'week041':
                        bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 1 по 5 число')
                        bot.send_message(call.message.chat.id, text='В среду будет мкр9 на монополию. Несколько маленьких задачек в сокративе (решать не на листочке). Я вам очень советую самостоятельно посмотреть и порешать задачи семинара 11, особенно пкрвые легкие. На семинаре все не успеем разобрать, потому что их много')
                    elif call.data == 'week042':
                        bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 6 по 12 число')
                        bot.send_message(call.message.chat.id, text='1. Завтра обсуждаем олигополию и кейсы из семинара 11. ВАЖНО! Изучите кейсы до семинара. На самом семинаре будете объяснять вы, а не, ответы на кейсы. Иначе просто помолчим дружно.')
                        bot.send_message(call.message.chat.id, text='2. Посмотрите лекцию «рынки с монопольной властью 2». Олигополия - сложная тема. Поэтому без базы будет сложно понять на семинаре.')
                        bot.send_message(call.message.chat.id, text='3. ‼️11.12 (в эту субботу) будет тестовая контрольная. По ее формату скажу позже (говорилось и на лекции). Это 10% от оценки. ')
                        bot.send_message(call.message.chat.id, text='4. До 16.12 надо сделать ИДЗ2 - анализ статьи. Критерии и что надо сделать смотрите в тимсе в файлах')
                    elif call.data == 'week043':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='кайфуем')
                    elif call.data == 'week044':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на чиле')
            #ВБИ
                    elif call.data == 'week051':
                        bot.send_message(call.message.chat.id, text='Хорошо, вот дз за неделю с 1 по 5 число')
                        bot.send_message(call.message.chat.id, text='Домашнее задание:')
                        bot.send_message(call.message.chat.id, text='Проектное задание')
                        bot.send_message(call.message.chat.id, text='1)Доработать MVP продукта. Если MVP готово или по MVP получены незначительные замечания, которые можно быстро доработать, то приступить к следующей функции (фиче) продукта.')
                        bot.send_message(call.message.chat.id, text='2)Описать процесс запуска MVP вашего продукта с помощью диаграммы Ганта.')
                        bot.send_message(call.message.chat.id, text='3)Заполнить таблицу по неделе 5 (Этап 5. Доработка продукта). Указать ссылки на доработанные задачи по каждой роли.')
                        bot.send_message(call.message.chat.id, text='Индивидуальное задание')
                        bot.send_message(call.message.chat.id, text='1)Для каждой модели ЖЦ (каскадная, гибкая, микс) привести по 2 примера сервисов/продуктов/ИС. Дать обоснование, почему для данного продукта подходит именно данная модель.')
                        bot.send_message(call.message.chat.id, text='2)Подготовиться к проверочной работе по учебнику Зараменских Е.П. «Основы бизнес-информатики» (главы 1-4)')




                    elif call.data == 'week052':


                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='кайфуем')
                    elif call.data == 'week053':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на расслабоне')
                    elif call.data == 'week054':
                        bot.send_message(call.message.chat.id, text='Домашнего задания пока нет')
                        bot.send_message(call.message.chat.id, text='пока на чиле')
                    if call.data == 'sub1':

                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week11'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week12'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week13'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week14'))

                        bot.send_message(message.chat.id, text='Окей, выберите учебный перод текущего месяца', reply_markup=menu1)

                    elif call.data == 'week11':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week12':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week13':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week14':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub2':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week21'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week22'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week23'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week24'))

                        bot.send_message(message.chat.id, text='Окей, выберите учебный перод текущего месяца', reply_markup=menu1)

                    elif call.data == 'week21':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week22':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week23':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week24':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub3':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week31'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week32'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week33'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week34'))

                        bot.send_message(message.chat.id, text='Окей, выберите учебный перод текущего месяца', reply_markup=menu1)

                    elif call.data == 'week31':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week32':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week33':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week34':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub4':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week41'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week42'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week43'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week44'))

                        bot.send_message(message.chat.id, text='Окей, выберите учебный перод текущего месяца', reply_markup=menu1)

                    elif call.data == 'week41':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week42':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week43':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week44':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub5':
                        menu1 = telebot.types.InlineKeyboardMarkup()
                        menu1.add(telebot.types.InlineKeyboardButton(text='1-5', callback_data='week1'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='6-12', callback_data='week2'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='13-19', callback_data='week3'))
                        menu1.add(telebot.types.InlineKeyboardButton(text='20-26', callback_data='week4'))

                        bot.send_message(message.chat.id, text='Окей, выберите учебный перод текущего месяца', reply_markup=menu1)

                    elif call.data == 'week51':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'week52':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week53':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')
                    elif call.data == 'week54':
                        bot.send_message(call.message.chat.id, text='Отравьте новое задание')

                    elif call.data == 'sub01':
                        bot.send_message(call.message.chat.id, text='Математический анализ')
                        bot.send_message(call.message.chat.id, text='Субочев Андрей Николаевич')
                        bot.send_message(call.message.chat.id, text='asubochev@hse.ru')
                    elif call.data == 'sub02':
                        bot.send_message(call.message.chat.id, text='Линейная Алгебра')
                        bot.send_message(call.message.chat.id, text='Широ́ков Дмитрий Сергеевич')
                        bot.send_message(call.message.chat.id, text='dshirokov@hse.ru, dm.shirokov@gmail.com')

                        bot.send_message(call.message.chat.id, text='Швыдун Сергей Владимирович')
                        bot.send_message(call.message.chat.id, text='shvydun@hse.ru')
                    elif call.data == 'sub03':
                        bot.send_message(call.message.chat.id, text='Дискретная Математика')
                        bot.send_message(call.message.chat.id, text='Шварц Дмитрий Александрович')
                        bot.send_message(call.message.chat.id, text='dshvarts@hse.ru')
                        bot.send_message(call.message.chat.id, text='Са́ночкин Юрий Ильич')
                        bot.send_message(call.message.chat.id, text='ysanochkin@hse.ru')


                    elif call.data == 'sub04':
                        bot.send_message(call.message.chat.id, text='Микроэкономика')
                        bot.send_message(call.message.chat.id, text='Аносова Анна Витальевна')
                        bot.send_message(call.message.chat.id, text='aanosova@hse.ru')
                        bot.send_message(call.message.chat.id, text='Кононова Наталия Вадимовна')
                        bot.send_message(call.message.chat.id, text='nvkononova@hse.ru')
                    elif call.data == 'sub05':
                        bot.send_message(call.message.chat.id, text='Введение в бизнес-информатику')
                        bot.send_message(call.message.chat.id, text='Зараменских Евгений Петрович')
                        bot.send_message(call.message.chat.id, text='ezaramenskikh@hse.ru')
                        bot.send_message(call.message.chat.id, text='Ефимов Андрей Евгеньевич')
                        bot.send_message(call.message.chat.id, text='aeefimov@hse.ru')
                        bot.send_message(call.message.chat.id, text='Давыденко Елизавета Алексеевна')
                        bot.send_message(call.message.chat.id, text='edavydenko@hse.ru')

                    elif call.data == 'sub12':
                        bot.send_message(call.message.chat.id, text='Линейная Алгебра')
                        bot.send_message(call.message.chat.id, text='Семинары Широкова Д.С.')
                        bot.send_message(call.message.chat.id,
                                         text='https://us02web.zoom.us/j/84287044609?pwd=Nzl3aDJYR1JvUFJNU2NSc1hOaGtIdz09#success')

                    elif call.data == 'sub13':
                        bot.send_message(call.message.chat.id, text='Дискретная Математика')
                        bot.send_message(call.message.chat.id, text='Семинары Шварца Д.А.')
                        bot.send_message(call.message.chat.id, text='код:520892')
                        bot.send_message(call.message.chat.id, text='https://us02web.zoom.us/j/86342035424#success')
                        bot.send_message(call.message.chat.id, text='Семинары Саночкина Ю.И.')
                        bot.send_message(call.message.chat.id, text='код:803036')
                        bot.send_message(call.message.chat.id, text='https://us02web.zoom.us/j/82382877097#success')


bot.polling(none_stop=True)

