from __future__ import annotations
from typing import Optional, List, Union

class ChatLocation:
    def __init__(
        self,
        location: 'Location',
        address: 'str'
    ):
        self.location = location
        self.address = address