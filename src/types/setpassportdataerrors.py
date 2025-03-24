from __future__ import annotations
from typing import Optional, List, Union

class setPassportDataErrors:
    def __init__(
        self,
        user_id: 'int',
        errors: 'List[PassportElementError]'
    ):
        self.user_id = user_id
        self.errors = errors