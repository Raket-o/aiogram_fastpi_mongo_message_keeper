"""The keyboard creation module."""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def cancel_buttons() -> InlineKeyboardMarkup:
    """
    Keyboard creation function.
    :return: InlineKeyboardMarkup
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Вернуться", callback_data="cancel_hand_1")
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
