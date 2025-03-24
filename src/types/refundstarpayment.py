from __future__ import annotations
from typing import Optional, List, Union

class refundStarPayment:
    def __init__(
        self,
        user_id: 'int',
        telegram_payment_charge_id: 'str'
    ):
        self.user_id = user_id
        self.telegram_payment_charge_id = telegram_payment_charge_id