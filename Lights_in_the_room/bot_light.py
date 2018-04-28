#!/usr/bin/python
import telegram
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import serial # if you have not already done so
import os,random
import picamera


bot = telegram.Bot(token="360805189:AAHSi6rhuQzint8OC_hRNMGnDlBpipOzvRY")
updater = Updater(token='360805189:AAHSi6rhuQzint8OC_hRNMGnDlBpipOzvRY')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
ser = serial.Serial('/dev/ttyUSB0', 9600)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a plant, please talk to me!")


def light(bot, update):
    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('/home/pi/plant/marina.jpg', 'rb'))
    ser.write('1')

def yellow(bot, update):
    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('/home/pi/plant/marina.jpg', 'rb'))
    ser.write('2')

def blue(bot, update):
    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('/home/pi/plant/marina.jpg', 'rb'))
    ser.write('3')

def rita(bot, update):
    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('/home/pi/Desktop/Light/Rita.jpg', 'rb'))
    ser.write('1')

def mama(bot, update):
    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    a=random.choice([x for x in os.listdir("/home/pi/Desktop/Light/mama") if
                  os.path.isfile(os.path.join("/home/pi/Desktop/Light/mama", x))])
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open(os.path.join("/home/pi/Desktop/Light/mama",a), 'rb'))

    ser.write(str(random.randint(2,5)))

def mugue(bot, update):
    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    a=random.choice([x for x in os.listdir("/home/pi/Desktop/Light/ilya") if
                  os.path.isfile(os.path.join("/home/pi/Desktop/Light/ilya", x))])
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open(os.path.join("/home/pi/Desktop/Light/ilya",a), 'rb'))
    ser.write("5")

def image(bot, update):

    #bot.sendPhoto(chat_id=update.message.chat_id, text="checking for water")
    camera = picamera.PiCamera()
    camera.rotation=270
    camera.vflip=True
    camera.hflip= True
    camera.capture('image.jpg')
    camera.close()

    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('/home/pi/plant/image.jpg', 'rb'))

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

start_handler = CommandHandler('start', start) # START
dispatcher.add_handler(start_handler)


light_handler = CommandHandler('light', light) # START
dispatcher.add_handler(light_handler)

yellow_handler = CommandHandler('yellow', yellow) # START
dispatcher.add_handler(yellow_handler)

blue_handler = CommandHandler('blue', blue) # START
dispatcher.add_handler(blue_handler)

rita_handler = CommandHandler('rita', rita) # START
dispatcher.add_handler(rita_handler)

mama_handler = CommandHandler('mama', mama) # START
dispatcher.add_handler(mama_handler)

mugue_handler = CommandHandler('mugue', mugue) # START
dispatcher.add_handler(mugue_handler)

image_handler = CommandHandler('image', image) # START
dispatcher.add_handler(image_handler)

echo_handler = MessageHandler(Filters.text, echo) # ECHO
dispatcher.add_handler(echo_handler)


unknown_handler = MessageHandler(Filters.command, unknown) # UNKNOWN
dispatcher.add_handler(unknown_handler)




updater.start_polling(poll_interval = 1.0,timeout=20)


updater.idle()
