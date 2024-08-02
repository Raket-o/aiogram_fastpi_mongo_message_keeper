"""The module for storing user data (states)."""

from aiogram.fsm.state import State, StatesGroup


class SendMessageState(StatesGroup):
    """Class RegisterUserState. Stores status information."""

    user_text = State()
