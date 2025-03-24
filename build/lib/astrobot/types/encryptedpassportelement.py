from __future__ import annotations
from typing import Optional, List, Union, Any

class EncryptedPassportElement:
    """EncryptedPassportElement Telegram API type"""

    def __init__(
        self,
        type: str,
        data: Optional[str],
        phone_number: Optional[str],
        email: Optional[str],
        files: Optional[List['PassportFile']],
        front_side: Optional['PassportFile'],
        reverse_side: Optional['PassportFile'],
        selfie: Optional['PassportFile'],
        translation: Optional[List['PassportFile']],
        hash: str
    ):
        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash
