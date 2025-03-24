from __future__ import annotations
from typing import Optional, List, Union

class restrictChatMember:
    def __init__(
        self,
        chat_id: 'Union[str]',
        user_id: 'int',
        permissions: 'ChatPermissions',
        use_independent_chat_permissions: 'Optional[bool]' = None,
        until_date: 'Optional[int]' = None
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.permissions = permissions
        self.use_independent_chat_permissions = use_independent_chat_permissions
        self.until_date = until_date