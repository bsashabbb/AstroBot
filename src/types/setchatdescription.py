from __future__ import annotations
from typing import Optional, List, Union

class setChatDescription:
    def __init__(
        self,
        chat_id: 'Union[str]',
        description: 'Optional[str]' = None
    ):
        self.chat_id = chat_id
        self.description = description