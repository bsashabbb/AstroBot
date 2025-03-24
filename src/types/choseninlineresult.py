from __future__ import annotations
from typing import Optional, List, Union

class ChosenInlineResult:
    def __init__(
        self,
        result_id: 'str',
        from_: 'User',
        query: 'str',
        location: 'Optional[Location]' = None,
        inline_message_id: 'Optional[str]' = None
    ):
        self.result_id = result_id
        self.from_ = from_
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query