from __future__ import annotations
from typing import Optional, List, Union

class deleteForumTopic:
    def __init__(
        self,
        chat_id: 'Union[str]',
        message_thread_id: 'int'
    ):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id