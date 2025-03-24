from __future__ import annotations
from typing import Optional, List, Union, Any

class GiveawayWinners:
    """GiveawayWinners Telegram API type"""

    def __init__(
        self,
        chat: 'Chat',
        giveaway_message_id: int,
        winners_selection_date: int,
        winner_count: int,
        winners: List['User'],
        additional_chat_count: Optional[int],
        prize_star_count: Optional[int],
        premium_subscription_month_count: Optional[int],
        unclaimed_prize_count: Optional[int],
        only_new_members: Optional[bool],
        was_refunded: Optional[bool],
        prize_description: Optional[str]
    ):
        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.winners = winners
        self.additional_chat_count = additional_chat_count
        self.prize_star_count = prize_star_count
        self.premium_subscription_month_count = premium_subscription_month_count
        self.unclaimed_prize_count = unclaimed_prize_count
        self.only_new_members = only_new_members
        self.was_refunded = was_refunded
        self.prize_description = prize_description
