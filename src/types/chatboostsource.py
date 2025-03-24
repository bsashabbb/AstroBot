from __future__ import annotations
from typing import Optional, List, Union

class ChatBoostSource:
    def __init__(
        self,
        source: 'str',
        user: 'User'
    ):
        self.source = source
        self.user = user