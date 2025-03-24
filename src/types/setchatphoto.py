from __future__ import annotations
from typing import Optional, List, Union

class setChatPhoto:
    def __init__(
        self,
        chat_id: 'Union[str]',
        photo: 'InputFile'
    ):
        self.chat_id = chat_id
        self.photo = photo