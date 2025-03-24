from __future__ import annotations
from typing import Optional, List, Union

class answerWebAppQuery:
    def __init__(
        self,
        web_app_query_id: 'str',
        result: 'InlineQueryResult'
    ):
        self.web_app_query_id = web_app_query_id
        self.result = result