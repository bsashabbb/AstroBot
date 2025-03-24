from __future__ import annotations
from typing import Optional, List, Union

class ReactionCount:
    def __init__(
        self,
        type: 'ReactionType',
        total_count: 'int'
    ):
        self.type = type
        self.total_count = total_count