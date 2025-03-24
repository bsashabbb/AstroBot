from __future__ import annotations
from typing import Optional, List, Union

class LinkPreviewOptions:
    def __init__(
        self,
        is_disabled: 'Optional[bool]' = None,
        url: 'Optional[str]' = None,
        prefer_small_media: 'Optional[bool]' = None,
        prefer_large_media: 'Optional[bool]' = None,
        show_above_text: 'Optional[bool]' = None
    ):
        self.is_disabled = is_disabled
        self.url = url
        self.prefer_small_media = prefer_small_media
        self.prefer_large_media = prefer_large_media
        self.show_above_text = show_above_text