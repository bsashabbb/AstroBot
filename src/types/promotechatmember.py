from __future__ import annotations
from typing import Optional, List, Union

class promoteChatMember:
    def __init__(
        self,
        chat_id: 'Union[str]',
        user_id: 'int',
        is_anonymous: 'Optional[bool]' = None,
        can_manage_chat: 'Optional[bool]' = None,
        can_delete_messages: 'Optional[bool]' = None,
        can_manage_video_chats: 'Optional[bool]' = None,
        can_restrict_members: 'Optional[bool]' = None,
        can_promote_members: 'Optional[bool]' = None,
        can_change_info: 'Optional[bool]' = None,
        can_invite_users: 'Optional[bool]' = None,
        can_post_stories: 'Optional[bool]' = None,
        can_edit_stories: 'Optional[bool]' = None,
        can_delete_stories: 'Optional[bool]' = None,
        can_post_messages: 'Optional[bool]' = None,
        can_edit_messages: 'Optional[bool]' = None,
        can_pin_messages: 'Optional[bool]' = None,
        can_manage_topics: 'Optional[bool]' = None
    ):
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_stories = can_post_stories
        self.can_edit_stories = can_edit_stories
        self.can_delete_stories = can_delete_stories
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics