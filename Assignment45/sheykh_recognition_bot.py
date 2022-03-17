import cv2
from tensorflow.keras.models import load_model
import numpy as np
import telebot

class SheykhRecognize:
    def __init__(self):
        self.model = load_model("E:\programming\PyLearn-SajjadAemmi\Assignment45\model\sheykhRecognition_model.h5")
        self.width = self.height = 224
        
    def predict(self, image_path):        
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (self.width, self.height))
        image = image / 255 
        image = image.reshape(1, self.width, self.height, 3)
        
        result = self.model.predict(image)
        pred = np.argmax(result)
        
        if pred == 0:
            answer = "She/He seems to be a normal person 👩👨"
        elif pred == 1:
            answer = "She/He seems to be a sheykh person 👳‍♂️"
            
        return answer
    
def get_image(person_image):
    try:
        name = person_image.photo[2].file_id
        image_path = name + '.jpg'
        file = bot.get_file(name)
        downloaded = bot.download_file(file.file_path)
        
        with open(f"E:\programming\PyLearn-SajjadAemmi\Assignment45\\bot\images\{image_path}", 'wb') as new:
            new.write(downloaded)
            
        pred = detector.predict(f"E:\programming\PyLearn-SajjadAemmi\Assignment45\\bot\images\{image_path}")
        bot.reply_to(person_image, pred)
        
    except:
        bot.reply_to(person_image, "Oops! Something is wrong ⚠\nPlease try again!")
    

detector = SheykhRecognize()
TOKEN = "5179753923:AAGlyrJ1UDjhTGf8OImGgH7346yQufXu4WA"
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['Start', 'start', 'شروع'])
def welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f'Hi {first_name} 👋')
    bot.send_message(message.chat.id, 'Click on /help for bot function 💡')
    
@bot.message_handler(commands=['Recognize', 'recognize', 'تشخیص'])
def detect(message):
    msg = bot.reply_to(message, 'Send a person image 📸\nPerson Category: 1. Normal  2. Sheykh')
    bot.register_next_step_handler(msg, get_image)
    
@bot.message_handler(commands=['Help', 'help', 'دستورالعمل'])
def myHelp(message):
    bot.reply_to(message, 'Send a person image with jpg or png format after click on \\recognize command\nProgrammer: Ali Yaghoubian 👨‍💻\nGithub link: https://github.com/AliYqb')
    
@bot.message_handler(func=lambda message: True)
def help(message):
    bot.reply_to(message, 'Click on help command to work with my bot')
    
bot.polling()