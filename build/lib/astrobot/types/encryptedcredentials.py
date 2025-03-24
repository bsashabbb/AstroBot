from __future__ import annotations
from typing import Optional, List, Union, Any

class EncryptedCredentials:
    """EncryptedCredentials Telegram API type"""

    def __init__(
        self,
        data: str,
        hash: str,
        secret: str
    ):
        self.data = data
        self.hash = hash
        self.secret = secret
