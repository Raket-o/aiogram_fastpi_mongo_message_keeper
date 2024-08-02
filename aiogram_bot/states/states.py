"""Модуль хранения данных (состояний) пользователя."""

from aiogram.fsm.state import State, StatesGroup


class SendMessageState(StatesGroup):
    """Класс RegisterUserState. Хранит информацию состояние."""

    user_text = State()
