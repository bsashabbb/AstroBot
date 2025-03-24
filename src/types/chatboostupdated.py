from __future__ import annotations
from typing import Optional, List, Union

class ChatBoostUpdated:
    def __init__(
        self,
        chat: 'Chat',
        boost: 'ChatBoost'
    ):
        self.chat = chat
        self.boost = boost