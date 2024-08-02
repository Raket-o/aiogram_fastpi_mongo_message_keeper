"""The module for processing the output of the message history."""
from aiogram import types

from keyboards.inline.cancel import cancel_buttons
from utils.api_manager import ApiManager

API_MANAGER = ApiManager()


async def message_history_1(
        message: [types.CallbackQuery, types.Message],
) -> None:
    """Displays the message history to the user."""
    status, response = await API_MANAGER.send_get(
        url="api/v1/messages/"
    )

    if status == 200:
        txt = "Конец списка"
        for message_user in response.get("messages"):
            await message.message.answer(f"""Пользователь: <b>{message_user.get('username')}</b>
Сообщение:
    <em>{message_user.get('message')}</em>""",
                parse_mode="HTML")
    else:
        txt = "Что-то пошло не так. Попробуйте ещё раз"

    kb = cancel_buttons()
    await message.message.answer(txt, reply_markup=kb)
