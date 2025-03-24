from __future__ import annotations
from typing import Optional, List, Union

class WriteAccessAllowed:
    def __init__(
        self,
        from_request: 'Optional[bool]' = None,
        web_app_name: 'Optional[str]' = None,
        from_attachment_menu: 'Optional[bool]' = None
    ):
        self.from_request = from_request
        self.web_app_name = web_app_name
        self.from_attachment_menu = from_attachment_menu