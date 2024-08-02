"""User status reset module."""

import logging

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.default_heandlers.start import start_command


async def cancel_handler_1(message: Message, state: FSMContext) -> None:
    """
    The /cancel command starts this function.
    The function resets the user's status.
    """
    logging.info("cancel_handler")
    await message.message.delete()
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(
            "Отмена",
            reply_markup=ReplyKeyboardRemove(),
        )

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Отмена",
        reply_markup=ReplyKeyboardRemove(),
    )

    await start_command(message)
