from __future__ import annotations
from typing import Optional, List, Union, Any

class WriteAccessAllowed:
    """WriteAccessAllowed Telegram API type"""

    def __init__(
        self,
        from_request: Optional[bool],
        web_app_name: Optional[str],
        from_attachment_menu: Optional[bool]
    ):
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu
