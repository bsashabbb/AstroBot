from __future__ import annotations
from typing import Optional, List, Union

class Giveaway:
    def __init__(
        self,
        chats: 'List[Chat]',
        winners_selection_date: 'int',
        winner_count: 'int',
        only_new_members: 'Optional[bool]' = None,
        has_public_winners: 'Optional[bool]' = None,
        prize_description: 'Optional[str]' = None,
        country_codes: 'Optional[List[str]]' = None,
        prize_star_count: 'Optional[int]' = None,
        premium_subscription_month_count: 'Optional[int]' = None
    ):
        self.chats = chats
        self.winners_selection_date = winners_selection_date
        self.winner_count = winner_count
        self.only_new_members = only_new_members
        self.has_public_winners = has_public_winners
        self.prize_description = prize_description
        self.country_codes = country_codes
        self.prize_star_count = prize_star_count
        self.premium_subscription_month_count = premium_subscription_month_count