import sqlite3
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from keyboards import start_keyboard, admin_keyboard

# Создаем или подключаемся к базе данных
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()

# Создаем таблицу пользователей, если ее нет
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    chat_id INTEGER,
    is_admin BOOLEAN DEFAULT 0
)
''')
conn.commit()

async def start_bot(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    chat_id = message.chat.id

    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()

    if user is None:
        cursor.execute('INSERT INTO users (user_id, username, chat_id) VALUES (?, ?, ?)', 
                       (user_id, username, chat_id))
        conn.commit()

    cursor.execute('SELECT is_admin FROM users WHERE user_id = ?', (user_id,))
    is_admin = cursor.fetchone()[0]

    if is_admin:
        await message.answer("Добро пожаловать, администратор!", reply_markup=start_keyboard)
    else:
        await message.answer("Добро пожаловать в бот!", reply_markup=start_keyboard)

async def get_users(message: Message):
    cursor.execute('SELECT user_id, username FROM users')
    users = cursor.fetchall()
    
    response = "Список пользователей:\n"
    for user_id, username in users:
        response += f"{user_id} - {username}\n"
    
    await message.answer(response, reply_markup=admin_keyboard)

async def add_admin(callback_query: CallbackQuery):
    await callback_query.message.answer("Введите ID пользователя для добавления в админы:")
    # Логика для добавления админа

async def remove_admin(callback_query: CallbackQuery):
    await callback_query.message.answer("Введите ID пользователя для удаления из админов:")
    # Логика для удаления админа
