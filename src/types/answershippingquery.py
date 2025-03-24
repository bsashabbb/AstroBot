from __future__ import annotations
from typing import Optional, List, Union

class answerShippingQuery:
    def __init__(
        self,
        shipping_query_id: 'str',
        ok: 'bool',
        shipping_options: 'Optional[List[ShippingOption]]' = None,
        error_message: 'Optional[str]' = None
    ):
        self.shipping_query_id = shipping_query_id
        self.ok = ok
        self.shipping_options = shipping_options
        self.error_message = error_message