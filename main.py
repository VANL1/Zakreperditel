import telebot
import config
from random import randint


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'pp', 'sigma'])
def start(message):
    if '/start' in message.text:
        bot.send_message(message.chat.id, "Пук пуги кагажки пертеж пипэски")
    elif '/pp' in message.text:
        x = randint(0, 8)
        bot.reply_to(message, config.penises[int(x)])
    elif '/sigma' in message.text:
        bot.send_photo(message.chat.id, photo=open('photo.jpeg', 'rb'))


@bot.message_handler(content_types=['text'])
def what(message):
    if message.text == 'Что?':
        sleep(2)
        bot.send_message(message.chat.id, "Паташти, йа ни такафарил")
        sleep(3)
        bot.send_message(message.chat.id, 'ЖОПА ПАНОС КАВНО')


@bot.message_handler(content_types=['poll'])
def f(message):
    bot.pin_chat_message(message.chat.id, message.id)


bot.polling(none_stop=True)
