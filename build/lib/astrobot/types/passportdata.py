from __future__ import annotations
from typing import Optional, List, Union, Any

class PassportData:
    """PassportData Telegram API type"""

    def __init__(
        self,
        data: List['EncryptedPassportElement'],
        credentials: 'EncryptedCredentials'
    ):
        self.data = data
        self.credentials = credentials
