from __future__ import annotations
from typing import Optional, List, Union, Any

class PassportFile:
    """PassportFile Telegram API type"""

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_size: int,
        file_date: int
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date
