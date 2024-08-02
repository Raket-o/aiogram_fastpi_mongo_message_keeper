"""Модуль создания клавиатуры."""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def greeting_buttons() -> InlineKeyboardMarkup:
    """
    Функция создания клавиатуры.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Отправить сообщение",
        callback_data="send_message_1"
    )
    keyboard_builder.button(text="История сообщений", callback_data="message_history_1")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
