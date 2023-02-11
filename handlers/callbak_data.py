import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username
import random
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001479839858

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):

    if call.data == 'go_1':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_2')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=17,reply_markup=markup)

    if call.data == 'go_2':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_3')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=23,reply_markup=markup)

    if call.data == 'go_3':
        change_status(call.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Let’s go 💵', url = 'https://t.me/BekirSPRINTbot?start=n_PocoLocoo')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=25)
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=27)
        await asyncio.sleep(25)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=29)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=30,reply_markup=markup)

    try:
        await bot.answer_callback_query(call.id)
    except:
        pass
