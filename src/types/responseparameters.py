from __future__ import annotations
from typing import Optional, List, Union

class ResponseParameters:
    def __init__(
        self,
        migrate_to_chat_id: 'Optional[int]' = None,
        retry_after: 'Optional[int]' = None
    ):
        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after