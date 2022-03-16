import telebot
from animalDetector_CNN_model import Animal_Detector_CNN

detector = Animal_Detector_CNN()
bot = telebot.TeleBot(token="TOKEN")

def get_image(user_image):
    try:
        name = user_image.photo[2].file_id
        image_path = name + '.jpg'
        file = bot.get_file(name)
        downloaded = bot.download_file(file.file_path)
        
        with open(f"E:\programming\PyLearn-SajjadAemmi\Assignment44\Animal_Detector\\bot\image\{image_path}", 'wb') as new:
            new.write(downloaded)
            
        pred = detector.predict(f"E:\programming\PyLearn-SajjadAemmi\Assignment44\Animal_Detector\\bot\image\{image_path}")
        bot.reply_to(user_image, pred)
        
    except:
        bot.reply_to(user_image, "Oops! Something is wrong ⚠\nPlease try again!")

@bot.message_handler(commands=['Start', 'start', 'شروع'])
def welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'Hi {first_name} 👋')
    bot.send_message(message.chat.id, 'Click on /help for bot function 💡')
    
@bot.message_handler(commands=['Detect', 'detect', 'تشخیص'])
def detect(message):
    msg = bot.reply_to(message, 'Send an animal picture with jpg or png format 📸\nAnimal Category: 1. Bee  2. Koala  3. Crocodile  4. Crow  5. Zebra')
    bot.register_next_step_handler(msg, get_image)
    
@bot.message_handler(commands=['Help', 'help', 'دستورالعمل'])
def myHelp(message):
    bot.reply_to(message, 'Send an animal picture with jpg or png format after click on detect command\nProgrammer: Ali Yaghoubian 👨‍💻\nGithub link: https://github.com/AliYqb')
    
@bot.message_handler(func=lambda message: True)
def help(message):
    bot.reply_to(message, 'Click on help command to work with my bot')
    
bot.polling()
