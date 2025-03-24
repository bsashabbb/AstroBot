from __future__ import annotations
from typing import Optional, List, Union

class answerPreCheckoutQuery:
    def __init__(
        self,
        pre_checkout_query_id: 'str',
        ok: 'bool',
        error_message: 'Optional[str]' = None
    ):
        self.pre_checkout_query_id = pre_checkout_query_id
        self.ok = ok
        self.error_message = error_message