from __future__ import annotations
from typing import Optional, List, Union, Any

class File:
    """File Telegram API type"""

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_size: Optional[int],
        file_path: Optional[str]
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path
