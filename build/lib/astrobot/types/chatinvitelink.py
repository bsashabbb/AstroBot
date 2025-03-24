from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatInviteLink:
    """ChatInviteLink Telegram API type"""

    def __init__(
        self,
        invite_link: str,
        creator: 'User',
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        name: Optional[str],
        expire_date: Optional[int],
        member_limit: Optional[int],
        pending_join_request_count: Optional[int],
        subscription_period: Optional[int],
        subscription_price: Optional[int]
    ):
        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count
        self.subscription_period = subscription_period
        self.subscription_price = subscription_price
