from __future__ import annotations
from typing import Optional, List, Union

class getStarTransactions:
    def __init__(
        self,
        offset: 'Optional[int]' = None,
        limit: 'Optional[int]' = None
    ):
        self.offset = offset
        self.limit = limit