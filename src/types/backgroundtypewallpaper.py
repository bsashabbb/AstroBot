from __future__ import annotations
from typing import Optional, List, Union

class BackgroundTypeWallpaper:
    def __init__(
        self,
        type: 'str',
        document: 'Document',
        dark_theme_dimming: 'int',
        is_blurred: 'Optional[bool]' = None,
        is_moving: 'Optional[bool]' = None
    ):
        self.type = type
        self.document = document
        self.dark_theme_dimming = dark_theme_dimming
        self.is_blurred = is_blurred
        self.is_moving = is_moving