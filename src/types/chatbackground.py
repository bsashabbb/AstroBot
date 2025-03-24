from __future__ import annotations
from typing import Optional, List, Union

class ChatBackground:
    def __init__(
        self,
        type: 'BackgroundType'
    ):
        self.type = type