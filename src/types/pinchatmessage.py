from __future__ import annotations
from typing import Optional, List, Union

class pinChatMessage:
    def __init__(
        self,
        chat_id: 'Union[str]',
        message_id: 'int',
        business_connection_id: 'Optional[str]' = None,
        disable_notification: 'Optional[bool]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.disable_notification = disable_notification