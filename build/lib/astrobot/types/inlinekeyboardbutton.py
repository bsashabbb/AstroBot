from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineKeyboardButton:
    """InlineKeyboardButton Telegram API type"""

    def __init__(
        self,
        text: str,
        url: Optional[str],
        callback_data: Optional[str],
        web_app: Optional['WebAppInfo'],
        login_url: Optional['LoginUrl'],
        switch_inline_query: Optional[str],
        switch_inline_query_current_chat: Optional[str],
        switch_inline_query_chosen_chat: Optional['SwitchInlineQueryChosenChat'],
        copy_text: Optional['CopyTextButton'],
        callback_game: Optional['CallbackGame'],
        pay: Optional[bool]
    ):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.copy_text = copy_text
        self.callback_game = callback_game
        self.pay = pay
