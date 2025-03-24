from __future__ import annotations
from typing import Optional, List, Union, Any

class VideoChatEnded:
    """VideoChatEnded Telegram API type"""

    def __init__(
        self,
        duration: int
    ):
        self.duration = duration
