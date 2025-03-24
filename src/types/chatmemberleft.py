from __future__ import annotations
from typing import Optional, List, Union

class ChatMemberLeft:
    def __init__(
        self,
        status: 'str',
        user: 'User'
    ):
        self.status = status
        self.user = user