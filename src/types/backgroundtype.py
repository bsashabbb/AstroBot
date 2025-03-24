from __future__ import annotations
from typing import Optional, List, Union

class BackgroundType:
    def __init__(
        self,
        type: 'str',
        fill: 'BackgroundFill',
        dark_theme_dimming: 'int'
    ):
        self.type = type
        self.fill = fill
        self.dark_theme_dimming = dark_theme_dimming