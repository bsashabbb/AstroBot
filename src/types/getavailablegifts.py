from __future__ import annotations
from typing import Optional, List, Union

class getAvailableGifts:
    def __init__(
        self,
        user_id: 'int',
        gift_id: 'str',
        pay_for_upgrade: 'Optional[bool]' = None,
        text: 'Optional[str]' = None,
        text_parse_mode: 'Optional[str]' = None,
        text_entities: 'Optional[List[MessageEntity]]' = None
    ):
        self.user_id = user_id
        self.gift_id = gift_id
        self.pay_for_upgrade = pay_for_upgrade
        self.text = text
        self.text_parse_mode = text_parse_mode
        self.text_entities = text_entities