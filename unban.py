from re import I
from subprocess import call
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
import os
from random import randint
from urllib.parse import urlparse
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import *
from random import choice
from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    PeerIdInvalid,
    UsernameNotOccupied,
    UserNotParticipant,
)
from enum import Enum
from pyrogram.types import Update
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, input_message_content, user_and_chats ,ReplyKeyboardMarkup ,ReplyKeyboardRemove
from pyrogram.types import ChatPermissions
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.raw.types import UpdateBotCallbackQuery


bot = Client(
    'all subject bot',
    api_id=7009965,
    api_hash="06651b174c4f0591deb0ed1e5663c996",
    bot_token="5530133288:AAHxF5_D6nNqHbRgWI-Klbt_iEzBRV5uZ0o",
    
)
START_MESSAGE='🔥Group menu🔥'
START_BUTTONS=[
    [InlineKeyboardButton('ENTER SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('SHARE CHANNEL',url='https://t.me/share/url?url=https%3A//t.me/BioVideoFullSyllubus')],
    [InlineKeyboardButton('SHARE GROUP',url='https://t.me/share/url?url=https://t.me/+ug3NYtaYPGY2MGE1')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
@bot.on_message(filters.command('menu')) #start
def start(bot, message):
    
    
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("unban"))
async def unb(_, message):
   done = 0
   async for m in bot.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
        try:
         await bot.unban_chat_member(message.chat.id, m.user.id)
         done += 1
        except:
         pass
         await message.reply(f"{done} users has been unbanned")

print("bot alive")
bot.run()