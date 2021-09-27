from enum import Flag
import random
import telebot

def hadsAdad(message):
    answer_number = random.randint(0, 1000)
    bot.send_message(message.chat.id, 'یک عدد بین ۰ تا ۱۰۰۰ بگو')
    flag = 0
    while True:
        @bot.message_handler(func=lambda message: True)
        def check_game(message):
            if int(message.text) > answer_number:
                bot.send_message(message.chat.id, 'کمترش کن')
            elif int(message.text) < answer_number:
                bot.send_message(message.chat.id, 'بیشترش کن')
            elif int(message.text) == answer_number:
                bot.send_message(message.chat.id, 'ماشالااااا خودشه\nپیداش کردی')
                flag = 1
        if flag == 1:
            break

bot = telebot.TeleBot("2019327355:AAF9JCQPiBsOQKrEivcNfGlAoFk5nWKQ0jc")

@bot.message_handler(['Start', 'start', 'شروع'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'{first_name} خوش اومدی')

@bot.message_handler(['Game', 'game', 'بازی'])
def play_game(message):
    bot.reply_to(message, 'بازی حدس عدد')
    hadsAdad(message)
    
bot.polling()