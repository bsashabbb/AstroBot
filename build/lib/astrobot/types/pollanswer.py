from __future__ import annotations
from typing import Optional, List, Union, Any

class PollAnswer:
    """PollAnswer Telegram API type"""

    def __init__(
        self,
        poll_id: str,
        voter_chat: Optional['Chat'],
        user: Optional['User'],
        option_ids: List[int]
    ):
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids
