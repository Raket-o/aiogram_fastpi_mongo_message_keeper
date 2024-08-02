"""The module for processing sending messages to the server."""

from aiogram import types
from aiogram.fsm.context import FSMContext

from aiogram_bot.handlers.default_heandlers.start import start_command
from aiogram_bot.keyboards.inline.cancel import cancel_buttons
from aiogram_bot.states.states import SendMessageState
from aiogram_bot.utils.api_manager import ApiManager

API_MANAGER = ApiManager()


async def message_send_1(
        message: types.Message, state: FSMContext
) -> None:
    """Waits for input from the user."""
    await message.message.delete()
    kb = cancel_buttons()
    await message.message.answer("Введите тест", reply_markup=kb)
    await state.set_state(SendMessageState.user_text)


async def message_send_2(
        message: types.Message,
        state: FSMContext
) -> None:
    """Sends a request to create a message."""
    user_text = message.text
    user_name = message.from_user.full_name if message.from_user.full_name else message.from_user.username
    await message.delete()

    data = {
        "username": user_name,
        "message": user_text,
    }

    status, response = await API_MANAGER.send_post(
        url="api/v1/messages/", json=data
    )

    if status == 201:
        txt = "Сообщение отправлено"
    else:
        txt = "Что-то пошло не так. Попробуйте ещё раз"

    await message.answer(txt)
    await start_command(message)
    await state.clear()
