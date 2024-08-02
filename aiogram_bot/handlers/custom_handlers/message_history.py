"""Модуль обработки создание привычки."""

import datetime

from aiogram import types
from aiogram.fsm.context import FSMContext

from aiogram_bot.handlers.default_heandlers.start import start_command
from aiogram_bot.keyboards.inline.cancel import cancel_buttons
from aiogram_bot.states.states import SendMessageState
from aiogram_bot.utils.api_manager import ApiManager

API_MANAGER = ApiManager()


async def message_history_1(
        message: [types.CallbackQuery, types.Message],
) -> None:
    """Функция message_history_1. Отправляет запрос на создание привычки."""
    await message.message.delete()

    status, response = await API_MANAGER.send_get(
        url="api/v1/messages/"
    )

    if status == 200:
        txt = "Конец списка"
        for message_user in response.get("messages"):
            print(message_user.get('username'))
            await message.message.answer(f"""Пользователь: {message_user.get('username')}
Сообщение: 
    {message_user.get('message')}""")
    else:
        txt = "Что-то пошло не так. Попробуйте ещё раз"

    kb = cancel_buttons()
    await message.message.answer(txt, reply_markup=kb)
