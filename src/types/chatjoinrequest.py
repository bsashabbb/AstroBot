from __future__ import annotations
from typing import Optional, List, Union

class ChatJoinRequest:
    def __init__(
        self,
        chat: 'Chat',
        from_: 'User',
        user_chat_id: 'int',
        date: 'int',
        bio: 'Optional[str]' = None,
        invite_link: 'Optional[ChatInviteLink]' = None
    ):
        self.chat = chat
        self.from_ = from_
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link