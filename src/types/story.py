from __future__ import annotations
from typing import Optional, List, Union

class Story:
    def __init__(
        self,
        chat: 'Chat',
        id: 'int'
    ):
        self.chat = chat
        self.id = id