from __future__ import annotations
from typing import Optional, List, Union, Any

class BusinessLocation:
    """BusinessLocation Telegram API type"""

    def __init__(
        self,
        address: str,
        location: Optional['Location']
    ):
        self.address = address
        self.location = location
