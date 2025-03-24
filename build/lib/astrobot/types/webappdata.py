from __future__ import annotations
from typing import Optional, List, Union, Any

class WebAppData:
    """WebAppData Telegram API type"""

    def __init__(
        self,
        data: str,
        button_text: str
    ):
        self.data = data
        self.button_text = button_text
