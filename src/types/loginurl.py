from __future__ import annotations
from typing import Optional, List, Union

class LoginUrl:
    def __init__(
        self,
        url: 'str',
        forward_text: 'Optional[str]' = None,
        bot_username: 'Optional[str]' = None,
        request_write_access: 'Optional[bool]' = None
    ):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access