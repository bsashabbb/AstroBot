from __future__ import annotations
from typing import Optional, List, Union

class EncryptedPassportElement:
    def __init__(
        self,
        type: 'str',
        hash: 'str',
        data: 'Optional[str]' = None,
        phone_number: 'Optional[str]' = None,
        email: 'Optional[str]' = None,
        files: 'Optional[List[PassportFile]]' = None,
        front_side: 'Optional[PassportFile]' = None,
        reverse_side: 'Optional[PassportFile]' = None,
        selfie: 'Optional[PassportFile]' = None,
        translation: 'Optional[List[PassportFile]]' = None
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