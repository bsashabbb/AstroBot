from __future__ import annotations
from typing import Optional, List, Union

class GeneralForumTopicUnhidden:
    def __init__(
        self,
        user_id: 'int',
        first_name: 'Optional[str]' = None,
        last_name: 'Optional[str]' = None,
        username: 'Optional[str]' = None,
        photo: 'Optional[List[PhotoSize]]' = None
    ):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.photo = photo