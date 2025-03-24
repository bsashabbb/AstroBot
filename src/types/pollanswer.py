from __future__ import annotations
from typing import Optional, List, Union

class PollAnswer:
    def __init__(
        self,
        poll_id: 'str',
        voter_chat: 'Optional[Chat]' = None,
        user: 'Optional[User]' = None,
        option_ids: 'Optional[List[int]]' = None
    ):
        self.poll_id = poll_id
        self.voter_chat = voter_chat
        self.user = user
        self.option_ids = option_ids