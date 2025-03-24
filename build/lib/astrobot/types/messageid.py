from __future__ import annotations
from typing import Optional, List, Union, Any

class MessageId:
    """MessageId Telegram API type"""

    def __init__(
        self,
        message_id: int
    ):
        self.message_id = message_id
