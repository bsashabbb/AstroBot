from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatJoinRequest:
    """ChatJoinRequest Telegram API type"""

    def __init__(
        self,
        chat: 'Chat',
        from_user: 'User',
        user_chat_id: int,
        date: int,
        bio: Optional[str],
        invite_link: Optional['ChatInviteLink']
    ):
        self.chat = chat
        self.from_user = from_user
        self.user_chat_id = user_chat_id
        self.date = date
        self.bio = bio
        self.invite_link = invite_link
