"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types
from OxfordLookUp import get_def
from googletrans import Translator
translator = Translator()

API_TOKEN = '5836943805:AAHwdIpUtkHkHeLHygfwrQinzVNVY8E09KQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi, I am created by @BloggeR1001")

@dp.message_handler(commands=['about'])
async  def about(message: types.Message):

    await message.answer("O.D.O ---  OFFICIAL DICS OF OXFORD ! ")





@dp.message_handler()
async def transltr(message: types.Message):
    # lang_detct = translator.detect(message.text).lang      # LANG DETECTOR 1!>>>>>>>>>>>......
    if len(message.text.split()) >= 2:     # YA'NI TEXT NI SPLIT()      YORDAMIDA , NECHTA SO'ZDAN IBORAT EKANLIGINI AJRATSA : .......
        await message.answer("Please send only one word !")
    #     trans2 = 'uz' if lang_detct=='en' else 'en'
    #
    #     await message.reply((translator.translate(message.text, trans2)).text)  # ALBATTA OXIRI END FINISH WITH .TEXT FOR SENDING PURPOSES 1!>>>>>>>.>....
    #     # # # REPLY NI O'RNIGA Message.Answer ham bo'laveradi , ASLIDA, PROSTA REPLAY , BIZMNING GAPIMIZGA ATVER ASNWER SIFATIDA QAYTARADI    1!>>>>>>>>>>>>............
    # else:
    #     if lang_detct == 'en':
    #         word_id = message.text
    #     else:
    #         word_id = translator.translate(message.text, trans2='en').text
    #
    elif get_def(message.text):
        await message.reply(f"Word : {message.text} \nDefinitions : \n{get_def(message.text)['definitions']}")
        if get_def(message.text).get('audio'):  # GET
            await message.reply_voice(get_def(message.text)['audio'])       # REPLY_VOICE   , AUDIOS SAHKLIDA QAYTARADI    1!>.........
                # # # ASLIDA, TELEGRAM MESSAGE REQUIRMENTLARI , SHUKI , AUIDIO FILES "OOG" , SHAKLIDA BO'LISHI , IF BIZDA, MP3 EXIST BO'LSA, REPLY_AUDIO . NI QO'LLASHIMIZ , KERAKKKK  1!>.......
        else:
                await message.reply("There isn't such kind of word / Bunday so'z Mavjuda Emas !")        # IF VALUE == FALSE








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#

# https://youtu.be/b6w9lS-OkPo

# heroku git:remote -a "name"



















