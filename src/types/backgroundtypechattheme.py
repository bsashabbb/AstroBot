from __future__ import annotations
from typing import Optional, List, Union

class BackgroundTypeChatTheme:
    def __init__(
        self,
        type: 'str',
        theme_name: 'str'
    ):
        self.type = type
        self.theme_name = theme_name