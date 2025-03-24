from __future__ import annotations
from typing import Optional, List, Union

class getUpdates:
    def __init__(
        self,
        offset: 'Optional[int]' = None,
        limit: 'Optional[int]' = None,
        timeout: 'Optional[int]' = None,
        allowed_updates: 'Optional[List[str]]' = None
    ):
        self.offset = offset
        self.limit = limit
        self.timeout = timeout
        self.allowed_updates = allowed_updates