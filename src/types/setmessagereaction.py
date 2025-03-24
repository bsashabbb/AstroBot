from __future__ import annotations
from typing import Optional, List, Union

class setMessageReaction:
    def __init__(
        self,
        chat_id: 'Union[str]',
        message_id: 'int',
        reaction: 'Optional[List[ReactionType]]' = None,
        is_big: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.message_id = message_id
        self.reaction = reaction
        self.is_big = is_big