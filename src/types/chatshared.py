from __future__ import annotations
from typing import Optional, List, Union

class ChatShared:
    def __init__(
        self,
        request_id: 'int',
        chat_id: 'int',
        title: 'Optional[str]' = None,
        username: 'Optional[str]' = None,
        photo: 'Optional[List[PhotoSize]]' = None
    ):
        self.request_id = request_id
        self.chat_id = chat_id
        self.title = title
        self.username = username
        self.photo = photo