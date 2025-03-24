from __future__ import annotations
from typing import Optional, List, Union

class UsersShared:
    def __init__(
        self,
        request_id: 'int',
        users: 'List[SharedUser]'
    ):
        self.request_id = request_id
        self.users = users