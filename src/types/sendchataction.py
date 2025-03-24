from __future__ import annotations
from typing import Optional, List, Union

class sendChatAction:
    def __init__(
        self,
        chat_id: 'Union[str]',
        action: 'str',
        business_connection_id: 'Optional[str]' = None,
        message_thread_id: 'Optional[int]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.action = action