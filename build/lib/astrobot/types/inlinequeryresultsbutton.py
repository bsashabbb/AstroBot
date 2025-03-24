from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultsButton:
    """InlineQueryResultsButton Telegram API type"""

    def __init__(
        self,
        text: str,
        web_app: Optional['WebAppInfo'],
        start_parameter: Optional[str]
    ):
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter
