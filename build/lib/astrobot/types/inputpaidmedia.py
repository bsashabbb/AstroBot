from __future__ import annotations
from typing import Optional, List, Union, Any

class InputPaidMedia:
    """InputPaidMedia Telegram API type"""

    def __init__(
        self,
        type: str,
        media: str
    ):
        self.type = type
        self.media = media
