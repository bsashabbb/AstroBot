from __future__ import annotations
from typing import Optional, List, Union, Any

class InputContactMessageContent:
    """InputContactMessageContent Telegram API type"""

    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: Optional[str],
        vcard: Optional[str]
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
