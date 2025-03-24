from __future__ import annotations
from typing import Optional, List, Union, Any

class MenuButtonWebApp:
    """MenuButtonWebApp Telegram API type"""

    def __init__(
        self,
        type: str,
        text: str,
        web_app: 'WebAppInfo'
    ):
        self.type = type
        self.text = text
        self.web_app = web_app
