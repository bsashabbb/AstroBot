from __future__ import annotations
from typing import Optional, List, Union

class Contact:
    def __init__(
        self,
        phone_number: 'str',
        first_name: 'str',
        last_name: 'Optional[str]' = None,
        user_id: 'Optional[int]' = None,
        vcard: 'Optional[str]' = None
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard