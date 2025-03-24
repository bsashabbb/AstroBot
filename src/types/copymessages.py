from __future__ import annotations
from typing import Optional, List, Union

class copyMessages:
    def __init__(
        self,
        chat_id: 'Union[str]',
        from_chat_id: 'Union[str]',
        message_ids: 'List[int]',
        message_thread_id: 'Optional[int]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        remove_caption: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.from_chat_id = from_chat_id
        self.message_ids = message_ids
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.remove_caption = remove_caption