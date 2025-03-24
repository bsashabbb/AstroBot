from __future__ import annotations
from typing import Optional, List, Union

class KeyboardButtonRequestUsers:
    def __init__(
        self,
        request_id: 'int',
        user_is_bot: 'Optional[bool]' = None,
        user_is_premium: 'Optional[bool]' = None,
        max_quantity: 'Optional[int]' = None,
        request_name: 'Optional[bool]' = None,
        request_username: 'Optional[bool]' = None,
        request_photo: 'Optional[bool]' = None
    ):
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity
        self.request_name = request_name
        self.request_username = request_username
        self.request_photo = request_photo