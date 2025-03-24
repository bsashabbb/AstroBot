from __future__ import annotations
from typing import Optional, List, Union

class answerCallbackQuery:
    def __init__(
        self,
        callback_query_id: 'str',
        text: 'Optional[str]' = None,
        show_alert: 'Optional[bool]' = None,
        url: 'Optional[str]' = None,
        cache_time: 'Optional[int]' = None
    ):
        self.callback_query_id = callback_query_id
        self.text = text
        self.show_alert = show_alert
        self.url = url
        self.cache_time = cache_time