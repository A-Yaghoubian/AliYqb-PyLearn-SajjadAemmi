import random
import telebot
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode
import pysynth_b

TOKEN = '2019327355:AAF9JCQPiBsOQKrEivcNfGlAoFk5nWKQ0jc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['Start', 'start'])
def wellcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'Hey {first_name}, Welcome 😃')
    
@bot.message_handler(commands=['Music', 'music'])
def product_music(message):
    msg = bot.send_message(message.chat.id, "Enter your notes\nExample: ('c', 4), ('e', 4), ('g', 4), ('c5', -2), ('e6', 8), ('d#6', 2)")
    bot.register_next_step_handler(msg, music)
    
def music(message):
    try:
        song =  eval(message.text)
        pysynth_b.make_wav(song, fn = 'song.wav')
        your_song = open('song.wav', 'rb')
        bot.send_audio(message.chat.id, your_song)
    except Exception as e:
        # print(e)
        bot.send_message(message.chat.id, 'WARNING ⚠\nPlease try again')

@bot.message_handler(commands=['Game', 'game'])
def play_game(message):
    bot.reply_to(message, 'Guess the number 🎯')
    msg = bot.send_message(message.chat.id, 'Tell me a number between 0 and 1000 ...')
    bot.register_next_step_handler(msg, game)

def game(msg):
    ANSWER_NUMBER = random.randint(0, 1000)
    def game_works(message):
        markUp = telebot.types.ReplyKeyboardMarkup(row_width=1)
        button_1 = telebot.types.KeyboardButton('New Game ? 🤔')
        markUp.add(button_1)
        try:
            if int(message.text) > ANSWER_NUMBER:
                msg = bot.send_message(message.chat.id, 'Come DOWN :D', reply_markup=markUp)
                bot.register_next_step_handler(msg, game_works)
            elif int(message.text) < ANSWER_NUMBER:
                msg = bot.send_message(message.chat.id, 'Go UP :D', reply_markup=markUp)
                bot.register_next_step_handler(msg, game_works)
            elif int(message.text) == ANSWER_NUMBER:
                msg = bot.send_message(message.chat.id, "That's Right 😍\nGood job buddy 👊", reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
            elif message.text == 'New Game ? 🤔':
                print('1')
                bot.send_message(message.chat.id, 'Guess the number 🎯 \nTell me a number between 0 and 1000 ...', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
                bot.register_next_step_handler_by_chat_id(message.chat.id, game)
        except:
            bot.reply_to(message, 'Did something happen? 😟\nLeave the game to check the rest of your needs.', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    game_works(msg)
    
@bot.message_handler(commands=['Age', 'age'])
def calculate_age(message):
    msg = bot.send_message(message.chat.id, 'Please tell me your date of birth (Jalali-Shamsi)\n📌Example: 27/4/1379')
    bot.register_next_step_handler(msg, age_works)
    
def age_works(message):
    slash_counter = 0
    for letter in message.text:
        if letter == '/':
            slash_counter += 1
            
    if slash_counter == 2:
        input_text = message.text
        input_list = input_text.split('/')
        try:
            difference = JalaliDatetime.now() - JalaliDatetime(input_list[2], input_list[1], input_list[0])
            
            if ',' not in str(difference):
                y = 0
                m = 0
                d = 0
            else:
                difference = int(((str(difference)).split(' '))[0])
                y = difference // 365
                difference %= 365
                m = difference // 30
                difference %= 30
                d = difference
            
            if y < 0:
                bot.send_message(message.chat.id, 'Wrong input!')
            elif y != 0 and m == 0 and d == 0: # y
                bot.send_message(message.chat.id, f'HAPPY BIRTHDAY 🎈🎂\nYou are {y} years old 😍')
            elif y != 0 and m != 0 and d == 0: # y m 
                bot.send_message(message.chat.id, f'You are {y} years and {m} months old :)\nBe healthy ❤')
            elif y != 0 and m == 0 and d != 0: # y d
                bot.send_message(message.chat.id, f'You are {y} years and {d} days old :)\nBe healthy ❤')
            elif y != 0 and m != 0 and d != 0: # y m d
                bot.send_message(message.chat.id, f'You are {y} years, {m} months and {d} days old :)\nBe healthy ❤')
            elif y == 0 and m != 0 and d == 0: # m
                bot.send_message(message.chat.id, f'You are {m} months old :)\nBe healthy 🤍')
            elif y == 0 and m != 0 and d != 0: # m d
                bot.send_message(message.chat.id, f'You are {m} months and {d} days old :)\nBe healthy 🤍')
            elif y == 0 and m == 0 and d != 0: # d
                bot.send_message(message.chat.id, f'You are {d} days old :)\nBe healthy 🤍')    
            elif y == 0 and m == 0 and d == 0: # 
                bot.send_message(message.chat.id, 'Welcome to this world, my dear 🎊👶')
        except:
            bot.send_message(message.chat.id, 'Wrong input!')
    else:
        bot.send_message(message.chat.id, 'Wrong input!')
            
@bot.message_handler(commands=['Voice', 'voice'])
def voice_producer(message):
    msg = bot.send_message(message.chat.id, 'Enter your message')
    bot.register_next_step_handler(msg, voice_works)

def voice_works(message):
    try:
        message_text = message.text
        language = 'en'
        message_voice = gTTS(text=message_text, lang=language, slow=False)
        message_voice.save('your_voice.ogg')
        voice = open('your_voice.ogg', 'rb')
        bot.send_voice(message.chat.id, voice)
    except:
        bot.send_message(message.chat.id, 'WARNING ⚠\nPlease try again')

@bot.message_handler(commands=['Qrcode', 'qrcode'])
def qrcode_producer(message):
    msg = bot.send_message(message.chat.id, 'Enter text or web address or ...\n🔑 Example: www.google.com')
    bot.register_next_step_handler(msg, qrcode_works)
    
def qrcode_works(message):
    try:
        message_text = message.text
        qrcode_image = qrcode.make(message_text)
        qrcode_image.save('your_qrcode.png')
        qrCode = open('your_qrcode.png', 'rb')
        bot.send_photo(message.chat.id, qrCode)
    except:
        bot.send_message(message.chat.id, 'WARNING ⚠\nPlease try again')
                    
@bot.message_handler(commands=['max', 'Max', 'MAX'])
def maxx(message):
    Description = "Write a list of your numbers (each separated by a ',')\nI will find the largest number and tell you 😎"
    msg = bot.send_message(message.chat.id, Description)
    bot.register_next_step_handler(msg, max_works)

def max_works(message):
    try:
        numbers_text = message.text
        numbers_list = numbers_text.split(',')
        numbers_list = list(map(int, numbers_list))
        answer = str(max(numbers_list))
        bot.send_message(message.chat.id, f'The largest number is {answer}')
    except:
        bot.send_message(message.chat.id, "WARNING ⚠\nDo you just enter numbers and ','? 🤔\nPlease try again")

@bot.message_handler(commands=['argmax', 'Argmax'])
def argmaxx(message):
    Description = "Write a list of your numbers (each separated by a ',')\nI will find the largest number and tell you its index 🧠\nList index starts from 0 ☺"
    msg = bot.send_message(message.chat.id, Description)
    bot.register_next_step_handler(msg, arg_works)

def arg_works(message):
    try:
        numbers_text = message.text
        numbers_list = numbers_text.split(',')
        numbers_list = list(map(int, numbers_list))
        answer_1 = str(max(numbers_list))
        answer_2 = str(numbers_list.index(max(numbers_list)))
        bot.send_message(message.chat.id, f'The largest number: {answer_1}\nIts index: {answer_2}')
    except:
        bot.send_message(message.chat.id, "WARNING ⚠\nDo you just enter numbers and ','? 🤔\nPlease try again")

@bot.message_handler(commands=['help', 'Help', 'HELP'])
def help(message):
    Description = '1️⃣ /start : start and welcome\n 2️⃣ /game : Play game\n 3️⃣ /age : Your age\n 4️⃣ /voice : text to voice\n 5️⃣ /max : maximum in list\n 6️⃣ /argmax : highest number argument in list\n 7️⃣ /qrcode : product QR code\n 8️⃣ /music : product your music\n\nAli Yaghoubian 👨‍💻\nSupport: @Alijackoub'
    bot.send_message(message.chat.id, Description)

bot.polling()