from __future__ import annotations
from typing import Optional, List, Union

class SentWebAppMessage:
    def __init__(
        self,
        inline_message_id: 'Optional[str]' = None
    ):
        self.inline_message_id = inline_message_id