from __future__ import annotations
from typing import Optional, List, Union

class EncryptedCredentials:
    def __init__(
        self,
        data: 'str',
        hash: 'str',
        secret: 'str'
    ):
        self.data = data
        self.hash = hash
        self.secret = secret