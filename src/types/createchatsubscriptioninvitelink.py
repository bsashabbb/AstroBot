from __future__ import annotations
from typing import Optional, List, Union

class createChatSubscriptionInviteLink:
    def __init__(
        self,
        chat_id: 'Union[str]',
        subscription_period: 'int',
        subscription_price: 'int',
        name: 'Optional[str]' = None
    ):
        self.chat_id = chat_id
        self.name = name
        self.subscription_period = subscription_period
        self.subscription_price = subscription_price