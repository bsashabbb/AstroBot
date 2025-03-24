from __future__ import annotations
from typing import Optional, List, Union, Any

class LoginUrl:
    """LoginUrl Telegram API type"""

    def __init__(
        self,
        url: str,
        forward_text: Optional[str],
        bot_username: Optional[str],
        request_write_access: Optional[bool]
    ):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access
