from __future__ import annotations
from typing import Optional, List, Union, Any

class ChosenInlineResult:
    """ChosenInlineResult Telegram API type"""

    def __init__(
        self,
        result_id: str,
        from_user: 'User',
        location: Optional['Location'],
        inline_message_id: Optional[str],
        query: str
    ):
        self.result_id = result_id
        self.from_user = from_user
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query
