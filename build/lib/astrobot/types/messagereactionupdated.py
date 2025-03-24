from __future__ import annotations
from typing import Optional, List, Union, Any
from . import Chat, ReactionType, User

class MessageReactionUpdated:
    def __init__(
        self,
        chat: 'Chat',
        message_id: int,
        user: Optional['User'],
        actor_chat: Optional['Chat'],
        date: int,
        old_reaction: List[ReactionType],
        new_reaction: List[ReactionType]
    ):
        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reaction = old_reaction
        self.new_reaction = new_reaction
