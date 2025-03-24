from __future__ import annotations
from typing import Optional, List, Union

class BusinessLocation:
    def __init__(
        self,
        address: 'str',
        location: 'Optional[Location]' = None
    ):
        self.address = address
        self.location = location