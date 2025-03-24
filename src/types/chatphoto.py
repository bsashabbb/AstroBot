from __future__ import annotations
from typing import Optional, List, Union

class ChatPhoto:
    def __init__(
        self,
        small_file_id: 'str',
        small_file_unique_id: 'str',
        big_file_id: 'str',
        big_file_unique_id: 'str'
    ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id