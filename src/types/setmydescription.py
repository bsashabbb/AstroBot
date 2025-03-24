from __future__ import annotations
from typing import Optional, List, Union

class setMyDescription:
    def __init__(
        self,
        description: 'Optional[str]' = None,
        language_code: 'Optional[str]' = None
    ):
        self.description = description
        self.language_code = language_code