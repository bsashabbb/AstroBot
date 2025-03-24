from __future__ import annotations
from typing import Optional, List, Union, Any

class PassportElementErrorUnspecified:
    """PassportElementErrorUnspecified Telegram API type"""

    def __init__(
        self,
        source: str,
        type: str,
        element_hash: str,
        message: str
    ):
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message
