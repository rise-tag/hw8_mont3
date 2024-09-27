from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

start_buttons = [
    [KeyboardButton(text="Mailing"), KeyboardButton(text="Users")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True, one_time_keyboard=True)

admin_inline = [
    [InlineKeyboardButton(text="Добавить админа", callback_data='add_admin')],
    [InlineKeyboardButton(text="Удалить админа", callback_data='remove_admin')]
]
admin_keyboard = InlineKeyboardMarkup(inline_keyboard=admin_inline)
