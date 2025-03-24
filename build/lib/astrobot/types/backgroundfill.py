from __future__ import annotations
from typing import Optional, List, Union, Any

class BackgroundFill:
    """BackgroundFill Telegram API type"""

    def __init__(
        self,
        type: str,
        color: int
    ):
        self.type = type
        self.color = color
