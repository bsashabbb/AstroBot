from __future__ import annotations
from typing import Optional, List, Union

class verifyUser:
    def __init__(
        self,
        user_id: 'int',
        custom_description: 'Optional[str]' = None
    ):
        self.user_id = user_id
        self.custom_description = custom_description