from __future__ import annotations
from typing import Optional, List, Union

class UserProfilePhotos:
    def __init__(
        self,
        total_count: 'int',
        photos: 'List[List[PhotoSize]]'
    ):
        self.total_count = total_count
        self.photos = photos