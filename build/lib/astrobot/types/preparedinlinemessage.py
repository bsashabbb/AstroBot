from __future__ import annotations
from typing import Optional, List, Union, Any

class PreparedInlineMessage:
    """PreparedInlineMessage Telegram API type"""

    def __init__(
        self,
        id: str,
        expiration_date: int
    ):
        self.id = id
        self.expiration_date = expiration_date
