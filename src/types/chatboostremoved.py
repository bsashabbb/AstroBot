from __future__ import annotations
from typing import Optional, List, Union

class ChatBoostRemoved:
    def __init__(
        self,
        chat: 'Chat',
        boost_id: 'str',
        remove_date: 'int',
        source: 'ChatBoostSource'
    ):
        self.chat = chat
        self.boost_id = boost_id
        self.remove_date = remove_date
        self.source = source