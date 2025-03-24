from __future__ import annotations
from typing import Optional, List, Union

class Voice:
    def __init__(
        self,
        file_id: 'str',
        file_unique_id: 'str',
        duration: 'int',
        mime_type: 'Optional[str]' = None,
        file_size: 'Optional[int]' = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size