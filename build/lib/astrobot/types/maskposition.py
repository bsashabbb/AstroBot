from __future__ import annotations
from typing import Optional, List, Union, Any

class MaskPosition:
    """MaskPosition Telegram API type"""

    def __init__(
        self,
        point: str,
        x_shift: float,
        y_shift: float,
        scale: float
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale
