#!/usr/bin/env python3
import os
import telebot
from telebot.types import Message
import ai


BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hola"])
def send_welcome(message):
    bot.reply_to(message, ai.ai_reply(message))


@bot.message_handler(func=lambda msg: True)
def send_message(message):
    bot.reply_to(message, ai.ai_reply(message))


bot.infinity_polling()
