from aiogram import Bot, Dispatcher, executor, types
from requests import get
import funcs
import logging
import keyboard as kb



print("Bot starting")

API_TOKEN = "5830892238:AAEDGU5xmrAeS9ofo0C1RSefFwicRU8vvRA"
styles = {1: "Кубизм 🔶", 2: "Звёздная ночь ✨", 3: "Витраж 🪞", 4: "Крик 😱", 5: "Ундина (Юная американка, Танец) 💃", 6: "Большая волна в Канагаве 🌊"}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome_def(message: types.Message):
    await message.answer(f"Привет! Этот бот может обработать изображение 🖼 нейронной сетью 🧠.\nВот примеры различных эффектов:\n1 - {styles[1]}\n2 - {styles[2]}\n3 - {styles[3]}\n4 - {styles[4]}\n5 - {styles[5]}\n6 - {styles[6]}")    
    media = types.MediaGroup()
    for i in range(1, 7):
    	media.attach_photo(types.input_file.InputFile(path_or_bytesio=f"effects_imgs/neural-effect-{i}.jpg"))
    await bot.send_media_group(chat_id=message.chat.id, media=media)
    await message.answer("Какой эффект будем использовать?", reply_markup=kb.inline_kb1)



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('effect'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    global effect
    effect = int(callback_query.data[-1])
    await bot.answer_callback_query(callback_query.id, text=f'Выбран стиль {styles[effect]}')
    await callback_query.message.answer(f"Окей, выбран стиль {styles[effect]}\nОтправляй мне изображение, а дальше я всё сделаю сам 😊")
        

@dp.message_handler(content_types=['photo'])
async def send_ph(message: types.Message):
    await message.photo[-1].download(f"original/{message.from_user.id}.png")
    print(f"Img for user {message.from_user.id} uploading...")
    uploading = await message.answer("Загружаю файл... 🚀\nОбычно это длится не более 15 секунд⏳")
    funcs.imgua(f"{message.from_user.id}.png", effect)
    await uploading.delete()
    await bot.send_photo(chat_id=message.chat.id, photo=types.input_file.InputFile(path_or_bytesio=f"neuro/{message.from_user.id}.png"), caption="Вроде @ArtPunk_bot справился!  🎉")
    print("Done!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)