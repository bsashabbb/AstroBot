from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultsButton:
    def __init__(
        self,
        text: 'str',
        web_app: 'Optional[WebAppInfo]' = None,
        start_parameter: 'Optional[str]' = None
    ):
        self.text = text
        self.web_app = web_app
        self.start_parameter = start_parameter