from __future__ import annotations
from typing import Optional, List, Union

class KeyboardButton:
    def __init__(
        self,
        text: 'Optional[str]' = None,
        request_users: 'Optional[KeyboardButtonRequestUsers]' = None,
        request_chat: 'Optional[KeyboardButtonRequestChat]' = None,
        request_contact: 'Optional[bool]' = None,
        request_location: 'Optional[bool]' = None,
        request_poll: 'Optional[KeyboardButtonPollType]' = None,
        web_app: 'Optional[WebAppInfo]' = None
    ):
        self.text = text
        self.request_users = request_users
        self.request_chat = request_chat
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app