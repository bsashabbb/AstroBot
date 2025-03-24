from __future__ import annotations
from typing import Optional, List, Union

class setChatPermissions:
    def __init__(
        self,
        chat_id: 'Union[str]',
        permissions: 'ChatPermissions',
        use_independent_chat_permissions: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.permissions = permissions
        self.use_independent_chat_permissions = use_independent_chat_permissions