from __future__ import annotations
from typing import Optional, List, Union, Any

class ForceReply:
    """ForceReply Telegram API type"""

    def __init__(
        self,
        force_reply: bool,
        input_field_placeholder: Optional[str],
        selective: Optional[bool]
    ):
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective
