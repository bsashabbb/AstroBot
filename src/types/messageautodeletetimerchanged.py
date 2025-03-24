from __future__ import annotations
from typing import Optional, List, Union

class MessageAutoDeleteTimerChanged:
    def __init__(
        self,
        message_auto_delete_time: 'int'
    ):
        self.message_auto_delete_time = message_auto_delete_time