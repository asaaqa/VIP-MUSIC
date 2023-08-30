from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VipX import app


def back_stats_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="TOPMARKUPGET",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def overallback_stats_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def get_stats_markup(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo g",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_7"],
                    callback_data="TOPMARKUPGET",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_6"],
                    url=f"https://t.me/{app.username}?start=stats",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_5"],
                    callback_data="TopOverall g",
                ),
            ],
            sudo if status else not_sudo,
        ]
    )
    return upl


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo s",
        ),
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="💞إغلاق💞",
                ),
            ],
        ]
    )
    return upl


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="©الاحصائيات™",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def top_ten_stats_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_2"],
                    callback_data="© المسارات ©",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_1"],
                    callback_data="© الدردشة ©",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_3"],
                    callback_data="© المستخدمون ©",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_4"],
                    callback_data="© الاحصائيات ©",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="® العالمية ®",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl
