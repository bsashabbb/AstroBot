from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatBoost:
    """ChatBoost Telegram API type"""

    def __init__(
        self,
        boost_id: str,
        add_date: int,
        expiration_date: int,
        source: 'ChatBoostSource'
    ):
        self.boost_id = boost_id
        self.add_date = add_date
        self.expiration_date = expiration_date
        self.source = source
