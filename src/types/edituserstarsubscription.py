from __future__ import annotations
from typing import Optional, List, Union

class editUserStarSubscription:
    def __init__(
        self,
        user_id: 'int',
        telegram_payment_charge_id: 'str',
        is_canceled: 'bool'
    ):
        self.user_id = user_id
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.is_canceled = is_canceled