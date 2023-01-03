from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
            
inline_btn_1 = InlineKeyboardButton('Кубизм🔶', callback_data="effect1")
inline_btn_2 = InlineKeyboardButton('Звёздная ночь ✨', callback_data="effect2")
inline_btn_3 = InlineKeyboardButton('Витраж 🪞', callback_data="effect3")
inline_btn_4 = InlineKeyboardButton('Крик 😱', callback_data="effect4")
inline_btn_5 = InlineKeyboardButton('Ундина (Юная американка, Танец) 💃', callback_data="effect5")
inline_btn_6 = InlineKeyboardButton('Большая волна в Канагаве 🌊    ', callback_data="effect6")

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_3, inline_btn_4)
inline_kb1.add(inline_btn_2)
inline_kb1.add(inline_btn_5)
inline_kb1.add(inline_btn_6)

