import telebot
import bs_api
import config
from random import randint
from time import sleep
from chats import write_ids
from schedule import time_until_end_of_lesson
import tbank

bot = telebot.TeleBot(config.token_tg)


@bot.message_handler(commands=['start', 'pp', 'sigma', 'trophies', 'victories', 'total_sigma', 'github', 'end_lesson',
                               'money'])
def start(message):
    if '/start' in message.text:
        bot.send_message(message.chat.id, "Пук пуги кагажки пертеж пипэски")
        write_ids(message.chat.id)
    elif '/pp' in message.text:
        x = randint(0, 8)
        bot.reply_to(message, config.penises[int(x)])
    elif '/sigma' in message.text:
        bot.send_photo(message.chat.id, photo=open('photo.png', 'rb'))
    elif '/trophies' in message.text:
        bot.send_message(message.chat.id,
                         f'Сигма игрок в бравл старс {bs_api.nickname()} сейчас имеет \033{bs_api.trophies()}\033 кубков')
    elif '/victories' in message.text:
        bot.send_message(message.chat.id, f'Сигма игрок в бравл старс {bs_api.nickname()} сейчас имеет:\n'
                                          f'{bs_api.victories()[0]} побед в соло шд\n'
                                          f'{bs_api.victories()[1]} побед в дуо шд\n'
                                          f'{bs_api.victories()[2]} побед в 3 на 3')
    elif '/total_sigma' in message.text:
        bot.send_message(message.chat.id,
                         f'{bs_api.nickname()} НСТОЛЬКО СИГМА, ЧТО У НЕГО {bs_api.trophies()} КУБУОВ {bs_api.victories()[0]} ПОБЕД В СОЛО ШД,'
                         f'{bs_api.victories()[1]} ПОБЕД В ДУО ШД И '
                         f'{bs_api.victories()[2]} ПОБЕД B 3 НА 3, А СУММАРНО У НЕГО {bs_api.sum_victories()} ПОБЕД')
        bot.send_message(message.chat.id, 'ЕБАТЬ ОН СИГМА')
    elif '/github' in message.text:
        bot.send_message(message.chat.id, 'Ссылка на гитхаб с исходником https://github.com/VANL1/Zakreperditel')
    elif '/end_lesson' in message.text:
        bot.send_message(message.chat.id, time_until_end_of_lesson())
    elif '/money' in message.text:
        bot.send_message(message.chat.id, f'У Васи на брокерском счету {tbank.money()}рбулей')
        bot.send_message(message.chat.id, 'Ебать он бомж')


@bot.message_handler(content_types=['text'])
def what(message):
    if message.text == 'Что?':
        sleep(2)
        bot.reply_to(message, "Паташти, йа ни такафарил")
        sleep(3)
        bot.send_message(message.chat.id, 'ЖОПА ПАНОС КАВНО')
    elif message.text == 'ZOV':
        bot.send_message(message.chat.id, 'ГОЙДА')
    elif message.text == '1488':
        bot.send_message(message.chat.id, 'Молодцы, вы справились со своей первой загадкой!')
        sleep(2)
        bot.send_message(message.chat.id, 'Ваша вторая загадка - это ребус')
        sleep(2.2)
        bot.send_message(message.chat.id, 'Угадаете и вы переходите на следующий уровень\n'
                                          'Всего будет 3 уровня:\n'
                                          '1.Простой\n'
                                          '2.Посложнее\n'
                                          '3.Самый сложный')
        sleep(5)
        bot.send_message(message.chat.id, 'У вас будет на эти три ребуса всего одна неделя.\n'
                                          'Напишите "Яйца", как будете готовы угадывать')
        sleep(4)

        bot.send_message(message.chat.id, 'Если конечно...')
        sleep(2)
        bot.send_message(message.chat.id, 'Не боитесь')
    elif message.text.lower() == 'Яйца'.lower():
        bot.send_message(message.chat.id, 'ПЕРВЫЙ РЕБУС: \n'
                                          '🎮 в 🦑')
    elif message.text.lower() == 'Игра в кальмара'.lower():
        bot.send_message(message.chat.id, 'ВТОРОЙ РЕБУС: \n'
                                          'Если ты и вправду рассчитывал на ребус, хочу тебя огорчить, тут будет шифр')
        sleep(4)
        bot.send_message(message.chat.id, 'И если ты его разгадаешь, а ответ напишешь сюда, ты сможешь узнать секрет 3го задания')
        sleep(4)
        bot.send_message(message.chat.id, 'И чуть не забыл, проси подсказку если не будешь справляться(напаши "подсказка")')
        bot.send_message(message.chat.id, 'Удачи')
        bot.send_message(message.chat.id, 'Сам шифр:\n'
                                          'пытюбииыб нбобктщ')
    elif message.text.lower() == 'Подсказка'.lower():
        bot.send_message(message.chat.id, "Иди нафиг со своё подсказкой")
        sleep(2)
        bot.send_message(message.chat.id, "Сам думай")
    elif message.text.lower() == 'Тыквенные семечки'.lower():
        bot.send_message(message.chat.id, "Третий ребус пока не придумал")


@bot.message_handler(content_types=['poll'])
def f(message):
    bot.pin_chat_message(message.chat.id, message.id)


@bot.message_handler(content_types=['pinned_message'])
def delete_pin(message):
    bot.delete_message(message.chat.id, message.id)


@bot.message_handler(content_types=['video', 'photo'])
def delete_pin(message):
    if message.chat.id == 1036894021:
        with open('chats_ids.txt', 'r') as p:
            penis = []
            for g in p:
                penis.append(int(g[:-1]))
        for i in penis:
            if i < 0 and i != -1002066813369:
                if message.content_type == 'video':
                    bot.send_video(i, message.video.file_id)
                else:
                    bot.send_photo(i, message.photo[-1].file_id)


bot.polling(none_stop=True)
