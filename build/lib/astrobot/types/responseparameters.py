from __future__ import annotations
from typing import Optional, List, Union, Any

class ResponseParameters:
    """ResponseParameters Telegram API type"""

    def __init__(
        self,
        migrate_to_chat_id: Optional[int],
        retry_after: Optional[int]
    ):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after
