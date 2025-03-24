from __future__ import annotations
from typing import Optional, List, Union

class setChatMenuButton:
    def __init__(
        self,
        chat_id: 'Optional[int]' = None,
        menu_button: 'Optional[MenuButton]' = None
    ):
        self.chat_id = chat_id
        self.menu_button = menu_button