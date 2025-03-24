from __future__ import annotations
from typing import Optional, List, Union, Any

class KeyboardButtonRequestChat:
    """KeyboardButtonRequestChat Telegram API type"""

    def __init__(
        self,
        request_id: int,
        chat_is_channel: bool,
        chat_is_forum: Optional[bool],
        chat_has_username: Optional[bool],
        chat_is_created: Optional[bool],
        user_administrator_rights: Optional['ChatAdministratorRights'],
        bot_administrator_rights: Optional['ChatAdministratorRights'],
        bot_is_member: Optional[bool],
        request_title: Optional[bool],
        request_username: Optional[bool],
        request_photo: Optional[bool]
    ):
        self.request_id = request_id
        self.chat_is_channel = chat_is_channel
        self.chat_is_forum = chat_is_forum
        self.chat_has_username = chat_has_username
        self.chat_is_created = chat_is_created
        self.user_administrator_rights = user_administrator_rights
        self.bot_administrator_rights = bot_administrator_rights
        self.bot_is_member = bot_is_member
        self.request_title = request_title
        self.request_username = request_username
        self.request_photo = request_photo
