from __future__ import annotations
from typing import Optional, List, Union

class getUserProfilePhotos:
    def __init__(
        self,
        user_id: 'int',
        offset: 'Optional[int]' = None,
        limit: 'Optional[int]' = None
    ):
        self.user_id = user_id
        self.offset = offset
        self.limit = limit