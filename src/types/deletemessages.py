from __future__ import annotations
from typing import Optional, List, Union

class deleteMessages:
    def __init__(
        self,
        chat_id: 'Union[str]',
        message_ids: 'List[int]'
    ):
        self.chat_id = chat_id
        self.message_ids = message_ids