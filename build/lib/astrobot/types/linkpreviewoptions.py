from __future__ import annotations
from typing import Optional, List, Union, Any

class LinkPreviewOptions:
    """LinkPreviewOptions Telegram API type"""

    def __init__(
        self,
        is_disabled: Optional[bool],
        url: Optional[str],
        prefer_small_media: Optional[bool],
        prefer_large_media: Optional[bool],
        show_above_text: Optional[bool]
    ):
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text
