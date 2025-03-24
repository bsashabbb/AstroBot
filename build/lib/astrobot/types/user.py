from __future__ import annotations
from typing import Optional, List, Union, Any

class User:
    """User Telegram API type"""

    def __init__(
        self,
        id: int,
        is_bot: bool,
        first_name: str,
        last_name: Optional[str],
        username: Optional[str],
        language_code: Optional[str],
        is_premium: Optional[bool],
        added_to_attachment_menu: Optional[bool],
        can_join_groups: Optional[bool],
        can_read_all_group_messages: Optional[bool],
        supports_inline_queries: Optional[bool],
        can_connect_to_business: Optional[bool],
        has_main_web_app: Optional[bool]
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
        self.can_connect_to_business = can_connect_to_business
        self.has_main_web_app = has_main_web_app
