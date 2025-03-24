from __future__ import annotations
from typing import Optional, List, Union, Any

class ChatFullInfo:
    """ChatFullInfo Telegram API type"""

    def __init__(
        self,
        id: int,
        type: str,
        title: Optional[str],
        username: Optional[str],
        first_name: Optional[str],
        last_name: Optional[str],
        is_forum: Optional[bool],
        accent_color_id: int,
        max_reaction_count: int,
        photo: Optional['ChatPhoto'],
        active_usernames: Optional[List[str]],
        birthdate: Optional['Birthdate'],
        business_intro: Optional['BusinessIntro'],
        business_location: Optional['BusinessLocation'],
        business_opening_hours: Optional['BusinessOpeningHours'],
        personal_chat: Optional['Chat'],
        available_reactions: Optional[List['ReactionType']],
        background_custom_emoji_id: Optional[str],
        profile_accent_color_id: Optional[int],
        profile_background_custom_emoji_id: Optional[str],
        emoji_status_custom_emoji_id: Optional[str],
        emoji_status_expiration_date: Optional[int],
        bio: Optional[str],
        has_private_forwards: Optional[bool],
        has_restricted_voice_and_video_messages: Optional[bool],
        join_to_send_messages: Optional[bool],
        join_by_request: Optional[bool],
        description: Optional[str],
        invite_link: Optional[str],
        pinned_message: Optional['Message'],
        permissions: Optional['ChatPermissions'],
        can_send_paid_media: Optional[bool],
        slow_mode_delay: Optional[int],
        unrestrict_boost_count: Optional[int],
        message_auto_delete_time: Optional[int],
        has_aggressive_anti_spam_enabled: Optional[bool],
        has_hidden_members: Optional[bool],
        has_protected_content: Optional[bool],
        has_visible_history: Optional[bool],
        sticker_set_name: Optional[str],
        can_set_sticker_set: Optional[bool],
        custom_emoji_sticker_set_name: Optional[str],
        linked_chat_id: Optional[int],
        location: Optional['ChatLocation']
    ):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_forum = is_forum
        self.accent_color_id = accent_color_id
        self.max_reaction_count = max_reaction_count
        self.photo = photo
        self.active_usernames = active_usernames
        self.birthdate = birthdate
        self.business_intro = business_intro
        self.business_location = business_location
        self.business_opening_hours = business_opening_hours
        self.personal_chat = personal_chat
        self.available_reactions = available_reactions
        self.background_custom_emoji_id = background_custom_emoji_id
        self.profile_accent_color_id = profile_accent_color_id
        self.profile_background_custom_emoji_id = profile_background_custom_emoji_id
        self.emoji_status_custom_emoji_id = emoji_status_custom_emoji_id
        self.emoji_status_expiration_date = emoji_status_expiration_date
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.has_restricted_voice_and_video_messages = has_restricted_voice_and_video_messages
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.can_send_paid_media = can_send_paid_media
        self.slow_mode_delay = slow_mode_delay
        self.unrestrict_boost_count = unrestrict_boost_count
        self.message_auto_delete_time = message_auto_delete_time
        self.has_aggressive_anti_spam_enabled = has_aggressive_anti_spam_enabled
        self.has_hidden_members = has_hidden_members
        self.has_protected_content = has_protected_content
        self.has_visible_history = has_visible_history
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.custom_emoji_sticker_set_name = custom_emoji_sticker_set_name
        self.linked_chat_id = linked_chat_id
        self.location = location
