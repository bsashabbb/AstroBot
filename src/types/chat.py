from __future__ import annotations
from typing import Optional, List, Union

class Chat:
    def __init__(
        self,
        id: 'int',
        type: 'str',
        title: 'Optional[str]' = None,
        username: 'Optional[str]' = None,
        first_name: 'Optional[str]' = None,
        last_name: 'Optional[str]' = None,
        is_forum: 'Optional[bool]' = None
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum