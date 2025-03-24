from __future__ import annotations
from typing import Optional, List, Union, Any

class BackgroundTypeChatTheme:
    """BackgroundTypeChatTheme Telegram API type"""

    def __init__(
        self,
        type: str,
        theme_name: str
    ):
        self.type = type
        self.theme_name = theme_name
