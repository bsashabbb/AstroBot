from __future__ import annotations
from typing import Optional, List, Union

class InlineQuery:
    def __init__(
        self,
        id: 'str',
        from_: 'User',
        query: 'str',
        offset: 'str',
        chat_type: 'Optional[str]' = None,
        location: 'Optional[Location]' = None
    ):
        self.id = id
        self.from_ = from_
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location