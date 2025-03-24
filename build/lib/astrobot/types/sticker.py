from __future__ import annotations
from typing import Optional, List, Union, Any

class Sticker:
    """Sticker Telegram API type"""

    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        type: str,
        width: int,
        height: int,
        is_animated: bool,
        is_video: bool,
        thumbnail: Optional['PhotoSize'],
        emoji: Optional[str],
        set_name: Optional[str],
        premium_animation: Optional['File'],
        mask_position: Optional['MaskPosition'],
        custom_emoji_id: Optional[str],
        needs_repainting: Optional[bool],
        file_size: Optional[int]
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnail = thumbnail
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size
