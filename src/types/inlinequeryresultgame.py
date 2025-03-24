from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultGame:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        game_short_name: 'str',
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None
    ):
        self.type = type
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup