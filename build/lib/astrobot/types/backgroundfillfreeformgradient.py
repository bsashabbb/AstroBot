from __future__ import annotations
from typing import Optional, List, Union, Any

class BackgroundFillFreeformGradient:
    """BackgroundFillFreeformGradient Telegram API type"""

    def __init__(
        self,
        type: str,
        colors: List[int]
    ):
        self.type = type
        self.colors = colors
