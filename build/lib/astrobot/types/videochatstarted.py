from __future__ import annotations
from typing import Optional, List, Union, Any

class VideoChatStarted:
    """VideoChatStarted Telegram API type"""

    def __init__(
        self,
        duration: int
    ):
        self.duration = duration
