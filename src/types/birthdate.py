from __future__ import annotations
from typing import Optional, List, Union

class Birthdate:
    def __init__(
        self,
        day: 'int',
        month: 'int',
        year: 'Optional[int]' = None
    ):
        self.day = day
        self.month = month
        self.year = year