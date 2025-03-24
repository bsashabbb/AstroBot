from __future__ import annotations
from typing import Optional, List, Union, Any
from . import Chat, ChatInviteLink, ChatMember, User

class ChatMemberUpdated:
    def __init__(
        self,
        chat: 'Chat',
        from_user: 'User',
        date: int,
        old_chat_member: 'ChatMember',
        new_chat_member: 'ChatMember',
        invite_link: Optional['ChatInviteLink'],
        via_join_request: Optional[bool],
        via_chat_folder_invite_link: Optional[bool]
    ):
        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_join_request = via_join_request
        self.via_chat_folder_invite_link = via_chat_folder_invite_link
