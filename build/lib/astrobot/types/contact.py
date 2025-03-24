from __future__ import annotations
from typing import Optional, List, Union, Any

class Contact:
    """Contact Telegram API type"""

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str],
        user_id: Optional[int],
        vcard: Optional[str]
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard
