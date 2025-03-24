from __future__ import annotations
from typing import Optional, List, Union

class BusinessOpeningHoursInterval:
    def __init__(
        self,
        opening_minute: 'int',
        closing_minute: 'int'
    ):
        self.opening_minute = opening_minute
        self.closing_minute = closing_minute