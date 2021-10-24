import os
import telebot

bot = telebot.TeleBot("API KEY HEAR")

@bot.message_handler(commands-["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello ! I'm widmal chat bot")
    
@bot.message_handler(commands-["how"])
def send_message(message):
    bot.send_messege(message,"https://youtube.com/c/WITechZone_widmal")
    
bot.polling()