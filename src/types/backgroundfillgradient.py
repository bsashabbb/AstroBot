from __future__ import annotations
from typing import Optional, List, Union

class BackgroundFillGradient:
    def __init__(
        self,
        type: 'str',
        top_color: 'int',
        bottom_color: 'int',
        rotation_angle: 'int'
    ):
        self.type = type
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.rotation_angle = rotation_angle