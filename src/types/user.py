from __future__ import annotations
from typing import Optional, List, Union

class User:
    def __init__(
        self,
        id: 'int',
        is_bot: 'bool',
        first_name: 'str',
        last_name: 'Optional[str]' = None,
        username: 'Optional[str]' = None,
        language_code: 'Optional[str]' = None,
        is_premium: 'Optional[bool]' = None,
        added_to_attachment_menu: 'Optional[bool]' = None,
        can_join_groups: 'Optional[bool]' = None,
        can_read_all_group_messages: 'Optional[bool]' = None,
        supports_inline_queries: 'Optional[bool]' = None,
        can_connect_to_business: 'Optional[bool]' = None,
        has_main_web_app: 'Optional[bool]' = None
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