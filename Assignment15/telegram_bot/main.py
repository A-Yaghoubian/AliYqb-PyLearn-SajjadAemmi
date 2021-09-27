# import random
# import telebot

# bot = telebot.TeleBot("2019327355:AAF9JCQPiBsOQKrEivcNfGlAoFk5nWKQ0jc")
# markUp = telebot.types.ReplyKeyboardMarkup(row_width=3)
# button_1 = telebot.types.KeyboardButton('موسیقی')
# button_2 = telebot.types.KeyboardButton('ویدیو')
# button_3 = telebot.types.KeyboardButton('عکس')

# markUp.add(button_1, button_2, button_3)

# @bot.message_handler(commands=['start', 'Start'])
# def send_welcome(message):
#     bot.reply_to(message, 'سلام دوست من. وقتت بخیر')
    
# @bot.message_handler(commands=['help', 'Help', 'komak'])
# def help(message):
#     bot.reply_to(message, 'این فقط یک تست باته. پنیک نکن')

# @bot.message_handler(commands=['فال'])
# def send_فال(message):
#     answers = ['به فنا خواهی رفت' ,'به دیدار معشوق خوهی رفت' ,'به سفر خواهی رفت' ,'پولدار میشوی' ,'بدبخت تر خواهی شد']
#     answer = random.choice(answers)
#     bot.reply_to(message, answer)
    
# @bot.message_handler(commands=['download', 'Download', 'دانلود'])
# def download(message):
#     bot.reply_to(message, 'کدوم یکی رو لازم داری ؟', reply_markup=markUp)
    
    
# @bot.message_handler(func=lambda message: True)
# def simple_messages(message):
#     if message.text == 'سلام':
#         bot.reply_to(message, 'علیک سلام')
#     elif message.text == 'خوبی؟':
#         bot.reply_to(message, 'نه فقط تو خوبی')
#     elif message.text == 'چطوری جون دل؟':
#         bot.reply_to(message, 'الهی صد هزار مرتبه شکر')
#     elif message.text == 'بوس':
#         bot.reply_to(message, 'جووون')
#     elif message.text == 'دوست دارم':
#         bot.reply_to(message, 'قلب')
#     elif message.text == 'عکس':
#         photo = open('image/photo.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:    
#         # bot.reply_to(message, 'نمیفهمم چی میگی')
#         bot.send_message(message.chat.id, 'نمیفهمم چی میگی')

# bot.polling()