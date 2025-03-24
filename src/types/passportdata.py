from __future__ import annotations
from typing import Optional, List, Union

class PassportData:
    def __init__(
        self,
        data: 'List[EncryptedPassportElement]',
        credentials: 'EncryptedCredentials'
    ):
        self.data = data
        self.credentials = credentials