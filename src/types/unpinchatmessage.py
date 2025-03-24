from __future__ import annotations
from typing import Optional, List, Union

class unpinChatMessage:
    def __init__(
        self,
        chat_id: 'Union[str]',
        business_connection_id: 'Optional[str]' = None,
        message_id: 'Optional[int]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id