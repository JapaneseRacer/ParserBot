import telebot
import config
from telebot import types
import time
import json

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message,res=False):
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       btn1 = types.KeyboardButton("👋 Поздороваться")
       sti = open('static/sticker.webp', 'rb')
       markup.add(btn1)
       bot.send_sticker(message.chat.id , sti)
       bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать тебе,...введи кодовое слово.".format(message.from_user, bot.get_me()),
                     parse_mode='html',  reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
       #bot.send_message(message.chat.id,message.text)
       if(message.text.strip()=='👋 Поздороваться'):  
              bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать тебе,...введи кодовое слово.".format(message.from_user, bot.get_me()),
                     parse_mode='html')
       if(message.text.strip()=='хочусистему'):
              #bot.send_message(message.chat.id, "мониторю.....")
              def f():
                     with open('new.json', 'r') as j:
                            json_data = json.load(j)
                            i=0
                     print(json_data)
              


                     number = 0
                     max_number = 0

                     for x in json_data:
                            if x < 2:
                                   number += 1
                                   if number > max_number:
                                          max_number = number
                            else:
                                   number = 0

                     print(max_number)  # 4
       #              while float(json_data[i])<3:
         #                   i=i+1

           #          if  i>=2:
                     if max_number>=7:
                                   print(" СХЕМА >>> ")
                                   bot.send_message(message.chat.id,".....СХЕМА!!!!!!!.....")

              while True:
                     time.sleep(3)
                     f()
                     lalala(message)
          
       #RUN
if __name__=='__main__':
       bot.polling(none_stop=True)






       
