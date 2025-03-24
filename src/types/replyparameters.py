from __future__ import annotations
from typing import Optional, List, Union

class ReplyParameters:
    def __init__(
        self,
        message_id: 'int',
        chat_id: 'Optional[Union[str]]' = None,
        allow_sending_without_reply: 'Optional[bool]' = None,
        quote: 'Optional[str]' = None,
        quote_parse_mode: 'Optional[str]' = None,
        quote_entities: 'Optional[List[MessageEntity]]' = None,
        quote_position: 'Optional[int]' = None
    ):
        self.message_id = message_id
        self.chat_id = chat_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.quote = quote
        self.quote_parse_mode = quote_parse_mode
        self.quote_entities = quote_entities
        self.quote_position = quote_position