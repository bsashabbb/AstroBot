from __future__ import annotations
from typing import Optional, List, Union, Any

class KeyboardButton:
    """KeyboardButton Telegram API type"""

    def __init__(
        self,
        text: Optional[str],
        request_users: Optional['KeyboardButtonRequestUsers'],
        request_chat: Optional['KeyboardButtonRequestChat'],
        request_contact: Optional[bool],
        request_location: Optional[bool],
        request_poll: Optional['KeyboardButtonPollType'],
        web_app: Optional['WebAppInfo']
    ):
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app
