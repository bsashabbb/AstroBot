from __future__ import annotations
from typing import Optional, List, Union, Any

class SharedUser:
    """SharedUser Telegram API type"""

    def __init__(
        self,
        user_id: int,
        first_name: Optional[str],
        last_name: Optional[str],
        username: Optional[str],
        photo: Optional[List['PhotoSize']]
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo
