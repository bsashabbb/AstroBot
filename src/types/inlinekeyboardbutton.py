from __future__ import annotations
from typing import Optional, List, Union

class InlineKeyboardButton:
    def __init__(
        self,
        text: 'str',
        url: 'Optional[str]' = None,
        callback_data: 'Optional[str]' = None,
        web_app: 'Optional[WebAppInfo]' = None,
        login_url: 'Optional[LoginUrl]' = None,
        switch_inline_query: 'Optional[str]' = None,
        switch_inline_query_current_chat: 'Optional[str]' = None,
        switch_inline_query_chosen_chat: 'Optional[SwitchInlineQueryChosenChat]' = None,
        copy_text: 'Optional[CopyTextButton]' = None,
        callback_game: 'Optional[CallbackGame]' = None,
        pay: 'Optional[bool]' = None
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