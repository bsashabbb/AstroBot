from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatBackground:
    """ChatBackground Telegram API type"""

    def __init__(
        self,
        type: 'BackgroundType'
    ):
        self.type = type
