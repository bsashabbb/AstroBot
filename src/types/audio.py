from __future__ import annotations
from typing import Optional, List, Union

class Audio:
    def __init__(
        self,
        file_id: 'str',
        file_unique_id: 'str',
        duration: 'int',
        performer: 'Optional[str]' = None,
        title: 'Optional[str]' = None,
        file_name: 'Optional[str]' = None,
        mime_type: 'Optional[str]' = None,
        file_size: 'Optional[int]' = None,
        thumbnail: 'Optional[PhotoSize]' = None
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnail = thumbnail