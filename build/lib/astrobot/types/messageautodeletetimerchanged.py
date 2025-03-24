from __future__ import annotations
from typing import Optional, List, Union, Any

class MessageAutoDeleteTimerChanged:
    """MessageAutoDeleteTimerChanged Telegram API type"""

    def __init__(
        self,
        message_auto_delete_time: int
    ):
        self.message_auto_delete_time = message_auto_delete_time
