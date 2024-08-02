"""User Handler registration module."""

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from states.states import SendMessageState

from aiogram_bot.handlers.custom_handlers.message_history import message_history_1
from aiogram_bot.handlers.custom_handlers.message_send import (
    message_send_1,
    message_send_2,
)
from aiogram_bot.handlers.default_heandlers.cancel import cancel_handler_1
from aiogram_bot.handlers.default_heandlers.start import start_command


def register_routers(router: Router):
    """
    The register_routers function. Collects handlers in the main router.
    """
    router.message.register(start_command, CommandStart())
    router.callback_query.register(
        start_command,
        F.data.startswith("start_command=")
    )

    router.callback_query.register(
        message_send_1,
        F.data == "send_message_1"
    )
    router.callback_query.register(
        message_history_1,
        F.data == "message_history_1"
    )
    router.message.register(message_send_2, SendMessageState.user_text)

    router.callback_query.register(cancel_handler_1, F.data == "cancel_hand_1")
    router.message.register(cancel_handler_1, Command("cancel_hand_1"))
