from __future__ import annotations
from typing import Optional, List, Union, Any

class SentWebAppMessage:
    """SentWebAppMessage Telegram API type"""

    def __init__(
        self,
        inline_message_id: Optional[str]
    ):
        self.inline_message_id = inline_message_id
