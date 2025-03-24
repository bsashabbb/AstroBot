from __future__ import annotations
from typing import Optional, List, Union

class verifyChat:
    def __init__(
        self,
        chat_id: 'Union[str]',
        custom_description: 'Optional[str]' = None
    ):
        self.chat_id = chat_id
        self.custom_description = custom_description