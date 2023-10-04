from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="اوامر الادمن",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="اوامر التشغيل",
                    callback_data="help_callback hb2",
                ),
            ],
            [ 
                InlineKeyboardButton(
                    text="اوامر البوت",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="اوامر القناة",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="™ المطور ™",
                    callback_data="help_callback hb6",
                ),
           ],
           [
                InlineKeyboardButton(
                    text="® خاص بالمطور ®",
                    callback_data="help_callback hb7",
                ),
            ],
             mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎭 المــيوزگ 🎭",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons

