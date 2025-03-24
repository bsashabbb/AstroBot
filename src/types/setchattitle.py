from __future__ import annotations
from typing import Optional, List, Union

class setChatTitle:
    def __init__(
        self,
        chat_id: 'Union[str]',
        title: 'str'
    ):
        self.chat_id = chat_id
        self.title = title