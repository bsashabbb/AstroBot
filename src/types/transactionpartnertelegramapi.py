from __future__ import annotations
from typing import Optional, List, Union

class TransactionPartnerTelegramApi:
    def __init__(
        self,
        type: 'str',
        request_count: 'int'
    ):
        self.type = type
        self.request_count = request_count