from __future__ import annotations
from typing import Optional, List, Union

class declineChatJoinRequest:
    def __init__(
        self,
        chat_id: 'Union[str]',
        user_id: 'int'
    ):
        self.chat_id = chat_id
        self.user_id = user_id