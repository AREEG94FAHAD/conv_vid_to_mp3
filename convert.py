import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.util import content_type_media
from helper import get_random_string
from moviepy.editor import *

APITOKENCONVERTER = os.environ.get('APITOKENCONVERTER')

bot = telebot.TeleBot(APITOKENCONVERTER)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(
        message.chat.id, "To convert your video to MP3 Send it ")





@bot.message_handler(func=lambda message: True)
def message_handler(message):

    try:

        msg = bot.send_message(
        message.chat.id, "To convert your video to MP3 Send it ")

    except:
        bot.send_message(
            message.chat.id, 'Something went wrong try agin later')


@bot.message_handler(content_types=content_type_media)
def image_handler(message):

    # print(message)
    # try:

    
    fileID = message.video.file_id
    print(fileID)
    file_info = bot.get_file(fileID)
    videoName = get_random_string(16)
    audioName = get_random_string(16)

    downloaded_file = bot.download_file(file_info.file_path)
    with open(videoName+'.mp4', 'wb') as new_file:
        new_file.write(downloaded_file)

    videoFile = VideoFileClip(videoName+'.mp4')
    mp33 = videoFile.audio
    mp33.write_audiofile(audioName+'.mp3')
    mp33.close()
    videoFile.close()


    send_mp3= open(audioName+".mp3", 'rb')
    bot.reply_to(message, '10 second left ')
    bot.send_document(message.chat.id, send_mp3)
    
    send_mp3.close()
    
    os.remove(videoName+'.mp4')
    os.remove(audioName+'.mp3')

# except:
#     bot.send_message(message.chat.id,'Something went wrong try again later')



    # imageName = get_random_string(16)
    # videoFile = VideoFileClip(downloaded_file).audio
    # videoFile.write_audiofile("imageName.mp3")
    
    # bot.reply_to(message, '10 second left ')
    # bot.reply_to(message, '5 second left ')
    # chat_id = message.chat.id
    # doc = open(imageName, 'rb')
    # bot.send_document(chat_id, doc)
    # doc.close()
    # bot.reply_to(message, ' Thank you for useing this bot do want to use it again')
    # os.remove(imageName+".jpg")

    # except:
    #     bot.send_message(message.chat.id,'Something went wrong try again later')


bot.polling()


# from moviepy.editor import *
# videoFile = VideoFileClip("123.mp4").audio
# videoFile.write_audiofile("theaudio.mp3")
