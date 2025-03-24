from __future__ import annotations
from typing import Optional, List, Union

class BusinessMessagesDeleted:
    def __init__(
        self,
        business_connection_id: 'str',
        chat: 'Chat',
        message_ids: 'List[int]'
    ):
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.message_ids = message_ids