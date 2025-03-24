from __future__ import annotations
from typing import Optional, List, Union

class BusinessOpeningHours:
    def __init__(
        self,
        time_zone_name: 'str',
        opening_hours: 'List[BusinessOpeningHoursInterval]'
    ):
        self.time_zone_name = time_zone_name
        self.opening_hours = opening_hours