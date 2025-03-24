from __future__ import annotations
from typing import Optional, List, Union, Any
from . import Chat, ReactionCount

class MessageReactionCountUpdated:
    def __init__(
        self,
        chat: 'Chat',
        message_id: int,
        date: int,
        reactions: List[ReactionCount]
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions
