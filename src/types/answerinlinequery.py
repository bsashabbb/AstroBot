from __future__ import annotations
from typing import Optional, List, Union

class answerInlineQuery:
    def __init__(
        self,
        inline_query_id: 'str',
        results: 'List[InlineQueryResult]',
        cache_time: 'Optional[int]' = None,
        is_personal: 'Optional[bool]' = None,
        next_offset: 'Optional[str]' = None,
        button: 'Optional[InlineQueryResultsButton]' = None
    ):
        self.inline_query_id = inline_query_id
        self.results = results
        self.cache_time = cache_time
        self.is_personal = is_personal
        self.next_offset = next_offset
        self.button = button