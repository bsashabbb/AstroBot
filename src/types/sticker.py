from __future__ import annotations
from typing import Optional, List, Union

class Sticker:
    def __init__(
        self,
        file_id: 'str',
        file_unique_id: 'str',
        type: 'str',
        width: 'int',
        height: 'int',
        is_animated: 'bool',
        is_video: 'bool',
        thumbnail: 'Optional[PhotoSize]' = None,
        emoji: 'Optional[str]' = None,
        set_name: 'Optional[str]' = None,
        premium_animation: 'Optional[File]' = None,
        mask_position: 'Optional[MaskPosition]' = None,
        custom_emoji_id: 'Optional[str]' = None,
        needs_repainting: 'Optional[bool]' = None,
        file_size: 'Optional[int]' = None
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