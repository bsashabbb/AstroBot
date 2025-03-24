from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatLocation:
    """ChatLocation Telegram API type"""

    def __init__(
        self,
        location: 'Location',
        address: str
    ):
        self.location = location
        self.address = address
