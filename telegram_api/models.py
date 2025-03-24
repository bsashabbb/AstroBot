from typing import Optional, Union, List, Dict, Any

from datetime import datetime


class TypeChecker:
    @staticmethod
    def check(value: Any, expected_type: str) -> None:
        if value is None:
            return
            
        type_names = [t.strip() for t in expected_type.split("|")]
        
        for type_name in type_names:
            try:
                if isinstance(value, eval(type_name)):
                    return
            except TypeError:
                continue
                
        raise TypeError(f"Expected {expected_type}, got {type(value).__name__}")



class User:
    """This object represents a Telegram user or bot."""
    def __init__(self, **kwargs: Any):
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']
        self._is_bot = None
        if 'is_bot' in kwargs:
            self.is_bot = kwargs['is_bot']
        self._first_name = None
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        self._last_name = None
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        self._username = None
        if 'username' in kwargs:
            self.username = kwargs['username']
        self._language_code = None
        if 'language_code' in kwargs:
            self.language_code = kwargs['language_code']
        self._is_premium = None
        if 'is_premium' in kwargs:
            self.is_premium = kwargs['is_premium']
        self._added_to_attachment_menu = None
        if 'added_to_attachment_menu' in kwargs:
            self.added_to_attachment_menu = kwargs['added_to_attachment_menu']
        self._can_join_groups = None
        if 'can_join_groups' in kwargs:
            self.can_join_groups = kwargs['can_join_groups']
        self._can_read_all_group_messages = None
        if 'can_read_all_group_messages' in kwargs:
            self.can_read_all_group_messages = kwargs['can_read_all_group_messages']
        self._supports_inline_queries = None
        if 'supports_inline_queries' in kwargs:
            self.supports_inline_queries = kwargs['supports_inline_queries']
        self._can_connect_to_business = None
        if 'can_connect_to_business' in kwargs:
            self.can_connect_to_business = kwargs['can_connect_to_business']
        self._has_main_web_app = None
        if 'has_main_web_app' in kwargs:
            self.has_main_web_app = kwargs['has_main_web_app']

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._id = value

    @property
    def is_bot(self) -> bool:
        return self._is_bot

    @is_bot.setter
    def is_bot(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_bot = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._first_name = value

    @property
    def last_name(self) -> str | None:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._last_name = value

    @property
    def username(self) -> str | None:
        return self._username

    @username.setter
    def username(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._username = value

    @property
    def language_code(self) -> str | None:
        return self._language_code

    @language_code.setter
    def language_code(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._language_code = value

    @property
    def is_premium(self) -> bool | None:
        return self._is_premium

    @is_premium.setter
    def is_premium(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_premium = value

    @property
    def added_to_attachment_menu(self) -> bool | None:
        return self._added_to_attachment_menu

    @added_to_attachment_menu.setter
    def added_to_attachment_menu(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._added_to_attachment_menu = value

    @property
    def can_join_groups(self) -> bool | None:
        return self._can_join_groups

    @can_join_groups.setter
    def can_join_groups(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_join_groups = value

    @property
    def can_read_all_group_messages(self) -> bool | None:
        return self._can_read_all_group_messages

    @can_read_all_group_messages.setter
    def can_read_all_group_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_read_all_group_messages = value

    @property
    def supports_inline_queries(self) -> bool | None:
        return self._supports_inline_queries

    @supports_inline_queries.setter
    def supports_inline_queries(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._supports_inline_queries = value

    @property
    def can_connect_to_business(self) -> bool | None:
        return self._can_connect_to_business

    @can_connect_to_business.setter
    def can_connect_to_business(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_connect_to_business = value

    @property
    def has_main_web_app(self) -> bool | None:
        return self._has_main_web_app

    @has_main_web_app.setter
    def has_main_web_app(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_main_web_app = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'is_bot': self._is_bot,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'username': self._username,
            'language_code': self._language_code,
            'is_premium': self._is_premium,
            'added_to_attachment_menu': self._added_to_attachment_menu,
            'can_join_groups': self._can_join_groups,
            'can_read_all_group_messages': self._can_read_all_group_messages,
            'supports_inline_queries': self._supports_inline_queries,
            'can_connect_to_business': self._can_connect_to_business,
            'has_main_web_app': self._has_main_web_app,
        }

class Chat:
    """This object represents a chat."""
    def __init__(self, **kwargs: Any):
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']
        self._username = None
        if 'username' in kwargs:
            self.username = kwargs['username']
        self._first_name = None
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        self._last_name = None
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        self._is_forum = None
        if 'is_forum' in kwargs:
            self.is_forum = kwargs['is_forum']

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._id = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def title(self) -> str | None:
        return self._title

    @title.setter
    def title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._title = value

    @property
    def username(self) -> str | None:
        return self._username

    @username.setter
    def username(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._username = value

    @property
    def first_name(self) -> str | None:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._first_name = value

    @property
    def last_name(self) -> str | None:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._last_name = value

    @property
    def is_forum(self) -> bool | None:
        return self._is_forum

    @is_forum.setter
    def is_forum(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_forum = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'type': self._type,
            'title': self._title,
            'username': self._username,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'is_forum': self._is_forum,
        }

class ChatFullInfo:
    """This object contains full information about a chat."""
    def __init__(self, **kwargs: Any):
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']
        self._username = None
        if 'username' in kwargs:
            self.username = kwargs['username']
        self._first_name = None
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        self._last_name = None
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        self._is_forum = None
        if 'is_forum' in kwargs:
            self.is_forum = kwargs['is_forum']
        self._accent_color_id = None
        if 'accent_color_id' in kwargs:
            self.accent_color_id = kwargs['accent_color_id']
        self._max_reaction_count = None
        if 'max_reaction_count' in kwargs:
            self.max_reaction_count = kwargs['max_reaction_count']
        self._photo = None
        if 'photo' in kwargs:
            self.photo = kwargs['photo']
        self._active_usernames = None
        if 'active_usernames' in kwargs:
            self.active_usernames = kwargs['active_usernames']
        self._birthdate = None
        if 'birthdate' in kwargs:
            self.birthdate = kwargs['birthdate']
        self._business_intro = None
        if 'business_intro' in kwargs:
            self.business_intro = kwargs['business_intro']
        self._business_location = None
        if 'business_location' in kwargs:
            self.business_location = kwargs['business_location']
        self._business_opening_hours = None
        if 'business_opening_hours' in kwargs:
            self.business_opening_hours = kwargs['business_opening_hours']
        self._personal_chat = None
        if 'personal_chat' in kwargs:
            self.personal_chat = kwargs['personal_chat']
        self._available_reactions = None
        if 'available_reactions' in kwargs:
            self.available_reactions = kwargs['available_reactions']
        self._background_custom_emoji_id = None
        if 'background_custom_emoji_id' in kwargs:
            self.background_custom_emoji_id = kwargs['background_custom_emoji_id']
        self._profile_accent_color_id = None
        if 'profile_accent_color_id' in kwargs:
            self.profile_accent_color_id = kwargs['profile_accent_color_id']
        self._profile_background_custom_emoji_id = None
        if 'profile_background_custom_emoji_id' in kwargs:
            self.profile_background_custom_emoji_id = kwargs['profile_background_custom_emoji_id']
        self._emoji_status_custom_emoji_id = None
        if 'emoji_status_custom_emoji_id' in kwargs:
            self.emoji_status_custom_emoji_id = kwargs['emoji_status_custom_emoji_id']
        self._emoji_status_expiration_date = None
        if 'emoji_status_expiration_date' in kwargs:
            self.emoji_status_expiration_date = kwargs['emoji_status_expiration_date']
        self._bio = None
        if 'bio' in kwargs:
            self.bio = kwargs['bio']
        self._has_private_forwards = None
        if 'has_private_forwards' in kwargs:
            self.has_private_forwards = kwargs['has_private_forwards']
        self._has_restricted_voice_and_video_messages = None
        if 'has_restricted_voice_and_video_messages' in kwargs:
            self.has_restricted_voice_and_video_messages = kwargs['has_restricted_voice_and_video_messages']
        self._join_to_send_messages = None
        if 'join_to_send_messages' in kwargs:
            self.join_to_send_messages = kwargs['join_to_send_messages']
        self._join_by_request = None
        if 'join_by_request' in kwargs:
            self.join_by_request = kwargs['join_by_request']
        self._description = None
        if 'description' in kwargs:
            self.description = kwargs['description']
        self._invite_link = None
        if 'invite_link' in kwargs:
            self.invite_link = kwargs['invite_link']
        self._pinned_message = None
        if 'pinned_message' in kwargs:
            self.pinned_message = kwargs['pinned_message']
        self._permissions = None
        if 'permissions' in kwargs:
            self.permissions = kwargs['permissions']
        self._can_send_gift = None
        if 'can_send_gift' in kwargs:
            self.can_send_gift = kwargs['can_send_gift']
        self._can_send_paid_media = None
        if 'can_send_paid_media' in kwargs:
            self.can_send_paid_media = kwargs['can_send_paid_media']
        self._slow_mode_delay = None
        if 'slow_mode_delay' in kwargs:
            self.slow_mode_delay = kwargs['slow_mode_delay']
        self._unrestrict_boost_count = None
        if 'unrestrict_boost_count' in kwargs:
            self.unrestrict_boost_count = kwargs['unrestrict_boost_count']
        self._message_auto_delete_time = None
        if 'message_auto_delete_time' in kwargs:
            self.message_auto_delete_time = kwargs['message_auto_delete_time']
        self._has_aggressive_anti_spam_enabled = None
        if 'has_aggressive_anti_spam_enabled' in kwargs:
            self.has_aggressive_anti_spam_enabled = kwargs['has_aggressive_anti_spam_enabled']
        self._has_hidden_members = None
        if 'has_hidden_members' in kwargs:
            self.has_hidden_members = kwargs['has_hidden_members']
        self._has_protected_content = None
        if 'has_protected_content' in kwargs:
            self.has_protected_content = kwargs['has_protected_content']
        self._has_visible_history = None
        if 'has_visible_history' in kwargs:
            self.has_visible_history = kwargs['has_visible_history']
        self._sticker_set_name = None
        if 'sticker_set_name' in kwargs:
            self.sticker_set_name = kwargs['sticker_set_name']
        self._can_set_sticker_set = None
        if 'can_set_sticker_set' in kwargs:
            self.can_set_sticker_set = kwargs['can_set_sticker_set']
        self._custom_emoji_sticker_set_name = None
        if 'custom_emoji_sticker_set_name' in kwargs:
            self.custom_emoji_sticker_set_name = kwargs['custom_emoji_sticker_set_name']
        self._linked_chat_id = None
        if 'linked_chat_id' in kwargs:
            self.linked_chat_id = kwargs['linked_chat_id']
        self._location = None
        if 'location' in kwargs:
            self.location = kwargs['location']

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._id = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def title(self) -> str | None:
        return self._title

    @title.setter
    def title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._title = value

    @property
    def username(self) -> str | None:
        return self._username

    @username.setter
    def username(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._username = value

    @property
    def first_name(self) -> str | None:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._first_name = value

    @property
    def last_name(self) -> str | None:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._last_name = value

    @property
    def is_forum(self) -> bool | None:
        return self._is_forum

    @is_forum.setter
    def is_forum(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_forum = value

    @property
    def accent_color_id(self) -> int:
        return self._accent_color_id

    @accent_color_id.setter
    def accent_color_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._accent_color_id = value

    @property
    def max_reaction_count(self) -> int:
        return self._max_reaction_count

    @max_reaction_count.setter
    def max_reaction_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._max_reaction_count = value

    @property
    def photo(self) -> ChatPhoto | None:
        return self._photo

    @photo.setter
    def photo(self, value: ChatPhoto | None) -> None:
        TypeChecker.check(value, 'ChatPhoto | None')
        self._photo = value

    @property
    def active_usernames(self) -> List[str] | None:
        return self._active_usernames

    @active_usernames.setter
    def active_usernames(self, value: List[str] | None) -> None:
        TypeChecker.check(value, 'List[str] | None')
        self._active_usernames = value

    @property
    def birthdate(self) -> Birthdate | None:
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value: Birthdate | None) -> None:
        TypeChecker.check(value, 'Birthdate | None')
        self._birthdate = value

    @property
    def business_intro(self) -> BusinessIntro | None:
        return self._business_intro

    @business_intro.setter
    def business_intro(self, value: BusinessIntro | None) -> None:
        TypeChecker.check(value, 'BusinessIntro | None')
        self._business_intro = value

    @property
    def business_location(self) -> BusinessLocation | None:
        return self._business_location

    @business_location.setter
    def business_location(self, value: BusinessLocation | None) -> None:
        TypeChecker.check(value, 'BusinessLocation | None')
        self._business_location = value

    @property
    def business_opening_hours(self) -> BusinessOpeningHours | None:
        return self._business_opening_hours

    @business_opening_hours.setter
    def business_opening_hours(self, value: BusinessOpeningHours | None) -> None:
        TypeChecker.check(value, 'BusinessOpeningHours | None')
        self._business_opening_hours = value

    @property
    def personal_chat(self) -> Chat | None:
        return self._personal_chat

    @personal_chat.setter
    def personal_chat(self, value: Chat | None) -> None:
        TypeChecker.check(value, 'Chat | None')
        self._personal_chat = value

    @property
    def available_reactions(self) -> List[ReactionType] | None:
        return self._available_reactions

    @available_reactions.setter
    def available_reactions(self, value: List[ReactionType] | None) -> None:
        TypeChecker.check(value, 'List[ReactionType] | None')
        self._available_reactions = value

    @property
    def background_custom_emoji_id(self) -> str | None:
        return self._background_custom_emoji_id

    @background_custom_emoji_id.setter
    def background_custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._background_custom_emoji_id = value

    @property
    def profile_accent_color_id(self) -> int | None:
        return self._profile_accent_color_id

    @profile_accent_color_id.setter
    def profile_accent_color_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._profile_accent_color_id = value

    @property
    def profile_background_custom_emoji_id(self) -> str | None:
        return self._profile_background_custom_emoji_id

    @profile_background_custom_emoji_id.setter
    def profile_background_custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._profile_background_custom_emoji_id = value

    @property
    def emoji_status_custom_emoji_id(self) -> str | None:
        return self._emoji_status_custom_emoji_id

    @emoji_status_custom_emoji_id.setter
    def emoji_status_custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._emoji_status_custom_emoji_id = value

    @property
    def emoji_status_expiration_date(self) -> int | None:
        return self._emoji_status_expiration_date

    @emoji_status_expiration_date.setter
    def emoji_status_expiration_date(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._emoji_status_expiration_date = value

    @property
    def bio(self) -> str | None:
        return self._bio

    @bio.setter
    def bio(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._bio = value

    @property
    def has_private_forwards(self) -> bool | None:
        return self._has_private_forwards

    @has_private_forwards.setter
    def has_private_forwards(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_private_forwards = value

    @property
    def has_restricted_voice_and_video_messages(self) -> bool | None:
        return self._has_restricted_voice_and_video_messages

    @has_restricted_voice_and_video_messages.setter
    def has_restricted_voice_and_video_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_restricted_voice_and_video_messages = value

    @property
    def join_to_send_messages(self) -> bool | None:
        return self._join_to_send_messages

    @join_to_send_messages.setter
    def join_to_send_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._join_to_send_messages = value

    @property
    def join_by_request(self) -> bool | None:
        return self._join_by_request

    @join_by_request.setter
    def join_by_request(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._join_by_request = value

    @property
    def description(self) -> str | None:
        return self._description

    @description.setter
    def description(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._description = value

    @property
    def invite_link(self) -> str | None:
        return self._invite_link

    @invite_link.setter
    def invite_link(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._invite_link = value

    @property
    def pinned_message(self) -> Message | None:
        return self._pinned_message

    @pinned_message.setter
    def pinned_message(self, value: Message | None) -> None:
        TypeChecker.check(value, 'Message | None')
        self._pinned_message = value

    @property
    def permissions(self) -> ChatPermissions | None:
        return self._permissions

    @permissions.setter
    def permissions(self, value: ChatPermissions | None) -> None:
        TypeChecker.check(value, 'ChatPermissions | None')
        self._permissions = value

    @property
    def can_send_gift(self) -> bool | None:
        return self._can_send_gift

    @can_send_gift.setter
    def can_send_gift(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_gift = value

    @property
    def can_send_paid_media(self) -> bool | None:
        return self._can_send_paid_media

    @can_send_paid_media.setter
    def can_send_paid_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_paid_media = value

    @property
    def slow_mode_delay(self) -> int | None:
        return self._slow_mode_delay

    @slow_mode_delay.setter
    def slow_mode_delay(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._slow_mode_delay = value

    @property
    def unrestrict_boost_count(self) -> int | None:
        return self._unrestrict_boost_count

    @unrestrict_boost_count.setter
    def unrestrict_boost_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._unrestrict_boost_count = value

    @property
    def message_auto_delete_time(self) -> int | None:
        return self._message_auto_delete_time

    @message_auto_delete_time.setter
    def message_auto_delete_time(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._message_auto_delete_time = value

    @property
    def has_aggressive_anti_spam_enabled(self) -> bool | None:
        return self._has_aggressive_anti_spam_enabled

    @has_aggressive_anti_spam_enabled.setter
    def has_aggressive_anti_spam_enabled(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_aggressive_anti_spam_enabled = value

    @property
    def has_hidden_members(self) -> bool | None:
        return self._has_hidden_members

    @has_hidden_members.setter
    def has_hidden_members(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_hidden_members = value

    @property
    def has_protected_content(self) -> bool | None:
        return self._has_protected_content

    @has_protected_content.setter
    def has_protected_content(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_protected_content = value

    @property
    def has_visible_history(self) -> bool | None:
        return self._has_visible_history

    @has_visible_history.setter
    def has_visible_history(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_visible_history = value

    @property
    def sticker_set_name(self) -> str | None:
        return self._sticker_set_name

    @sticker_set_name.setter
    def sticker_set_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._sticker_set_name = value

    @property
    def can_set_sticker_set(self) -> bool | None:
        return self._can_set_sticker_set

    @can_set_sticker_set.setter
    def can_set_sticker_set(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_set_sticker_set = value

    @property
    def custom_emoji_sticker_set_name(self) -> str | None:
        return self._custom_emoji_sticker_set_name

    @custom_emoji_sticker_set_name.setter
    def custom_emoji_sticker_set_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._custom_emoji_sticker_set_name = value

    @property
    def linked_chat_id(self) -> int | None:
        return self._linked_chat_id

    @linked_chat_id.setter
    def linked_chat_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._linked_chat_id = value

    @property
    def location(self) -> ChatLocation | None:
        return self._location

    @location.setter
    def location(self, value: ChatLocation | None) -> None:
        TypeChecker.check(value, 'ChatLocation | None')
        self._location = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'type': self._type,
            'title': self._title,
            'username': self._username,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'is_forum': self._is_forum,
            'accent_color_id': self._accent_color_id,
            'max_reaction_count': self._max_reaction_count,
            'photo': self._photo,
            'active_usernames': self._active_usernames,
            'birthdate': self._birthdate,
            'business_intro': self._business_intro,
            'business_location': self._business_location,
            'business_opening_hours': self._business_opening_hours,
            'personal_chat': self._personal_chat,
            'available_reactions': self._available_reactions,
            'background_custom_emoji_id': self._background_custom_emoji_id,
            'profile_accent_color_id': self._profile_accent_color_id,
            'profile_background_custom_emoji_id': self._profile_background_custom_emoji_id,
            'emoji_status_custom_emoji_id': self._emoji_status_custom_emoji_id,
            'emoji_status_expiration_date': self._emoji_status_expiration_date,
            'bio': self._bio,
            'has_private_forwards': self._has_private_forwards,
            'has_restricted_voice_and_video_messages': self._has_restricted_voice_and_video_messages,
            'join_to_send_messages': self._join_to_send_messages,
            'join_by_request': self._join_by_request,
            'description': self._description,
            'invite_link': self._invite_link,
            'pinned_message': self._pinned_message,
            'permissions': self._permissions,
            'can_send_gift': self._can_send_gift,
            'can_send_paid_media': self._can_send_paid_media,
            'slow_mode_delay': self._slow_mode_delay,
            'unrestrict_boost_count': self._unrestrict_boost_count,
            'message_auto_delete_time': self._message_auto_delete_time,
            'has_aggressive_anti_spam_enabled': self._has_aggressive_anti_spam_enabled,
            'has_hidden_members': self._has_hidden_members,
            'has_protected_content': self._has_protected_content,
            'has_visible_history': self._has_visible_history,
            'sticker_set_name': self._sticker_set_name,
            'can_set_sticker_set': self._can_set_sticker_set,
            'custom_emoji_sticker_set_name': self._custom_emoji_sticker_set_name,
            'linked_chat_id': self._linked_chat_id,
            'location': self._location,
        }

class Message:
    """This object represents a message."""
    def __init__(self, **kwargs: Any):
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._message_thread_id = None
        if 'message_thread_id' in kwargs:
            self.message_thread_id = kwargs['message_thread_id']
        self._from_user = None
        if 'from_user' in kwargs:
            self.from_user = kwargs['from_user']
        self._sender_chat = None
        if 'sender_chat' in kwargs:
            self.sender_chat = kwargs['sender_chat']
        self._sender_boost_count = None
        if 'sender_boost_count' in kwargs:
            self.sender_boost_count = kwargs['sender_boost_count']
        self._sender_business_bot = None
        if 'sender_business_bot' in kwargs:
            self.sender_business_bot = kwargs['sender_business_bot']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._business_connection_id = None
        if 'business_connection_id' in kwargs:
            self.business_connection_id = kwargs['business_connection_id']
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._forward_origin = None
        if 'forward_origin' in kwargs:
            self.forward_origin = kwargs['forward_origin']
        self._is_topic_message = None
        if 'is_topic_message' in kwargs:
            self.is_topic_message = kwargs['is_topic_message']
        self._is_automatic_forward = None
        if 'is_automatic_forward' in kwargs:
            self.is_automatic_forward = kwargs['is_automatic_forward']
        self._reply_to_message = None
        if 'reply_to_message' in kwargs:
            self.reply_to_message = kwargs['reply_to_message']
        self._external_reply = None
        if 'external_reply' in kwargs:
            self.external_reply = kwargs['external_reply']
        self._quote = None
        if 'quote' in kwargs:
            self.quote = kwargs['quote']
        self._reply_to_story = None
        if 'reply_to_story' in kwargs:
            self.reply_to_story = kwargs['reply_to_story']
        self._via_bot = None
        if 'via_bot' in kwargs:
            self.via_bot = kwargs['via_bot']
        self._edit_date = None
        if 'edit_date' in kwargs:
            self.edit_date = kwargs['edit_date']
        self._has_protected_content = None
        if 'has_protected_content' in kwargs:
            self.has_protected_content = kwargs['has_protected_content']
        self._is_from_offline = None
        if 'is_from_offline' in kwargs:
            self.is_from_offline = kwargs['is_from_offline']
        self._media_group_id = None
        if 'media_group_id' in kwargs:
            self.media_group_id = kwargs['media_group_id']
        self._author_signature = None
        if 'author_signature' in kwargs:
            self.author_signature = kwargs['author_signature']
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._entities = None
        if 'entities' in kwargs:
            self.entities = kwargs['entities']
        self._link_preview_options = None
        if 'link_preview_options' in kwargs:
            self.link_preview_options = kwargs['link_preview_options']
        self._effect_id = None
        if 'effect_id' in kwargs:
            self.effect_id = kwargs['effect_id']
        self._animation = None
        if 'animation' in kwargs:
            self.animation = kwargs['animation']
        self._audio = None
        if 'audio' in kwargs:
            self.audio = kwargs['audio']
        self._document = None
        if 'document' in kwargs:
            self.document = kwargs['document']
        self._paid_media = None
        if 'paid_media' in kwargs:
            self.paid_media = kwargs['paid_media']
        self._photo = None
        if 'photo' in kwargs:
            self.photo = kwargs['photo']
        self._sticker = None
        if 'sticker' in kwargs:
            self.sticker = kwargs['sticker']
        self._story = None
        if 'story' in kwargs:
            self.story = kwargs['story']
        self._video = None
        if 'video' in kwargs:
            self.video = kwargs['video']
        self._video_note = None
        if 'video_note' in kwargs:
            self.video_note = kwargs['video_note']
        self._voice = None
        if 'voice' in kwargs:
            self.voice = kwargs['voice']
        self._caption = None
        if 'caption' in kwargs:
            self.caption = kwargs['caption']
        self._caption_entities = None
        if 'caption_entities' in kwargs:
            self.caption_entities = kwargs['caption_entities']
        self._show_caption_above_media = None
        if 'show_caption_above_media' in kwargs:
            self.show_caption_above_media = kwargs['show_caption_above_media']
        self._has_media_spoiler = None
        if 'has_media_spoiler' in kwargs:
            self.has_media_spoiler = kwargs['has_media_spoiler']
        self._contact = None
        if 'contact' in kwargs:
            self.contact = kwargs['contact']
        self._dice = None
        if 'dice' in kwargs:
            self.dice = kwargs['dice']
        self._game = None
        if 'game' in kwargs:
            self.game = kwargs['game']
        self._poll = None
        if 'poll' in kwargs:
            self.poll = kwargs['poll']
        self._venue = None
        if 'venue' in kwargs:
            self.venue = kwargs['venue']
        self._location = None
        if 'location' in kwargs:
            self.location = kwargs['location']
        self._new_chat_members = None
        if 'new_chat_members' in kwargs:
            self.new_chat_members = kwargs['new_chat_members']
        self._left_chat_member = None
        if 'left_chat_member' in kwargs:
            self.left_chat_member = kwargs['left_chat_member']
        self._new_chat_title = None
        if 'new_chat_title' in kwargs:
            self.new_chat_title = kwargs['new_chat_title']
        self._new_chat_photo = None
        if 'new_chat_photo' in kwargs:
            self.new_chat_photo = kwargs['new_chat_photo']
        self._delete_chat_photo = None
        if 'delete_chat_photo' in kwargs:
            self.delete_chat_photo = kwargs['delete_chat_photo']
        self._group_chat_created = None
        if 'group_chat_created' in kwargs:
            self.group_chat_created = kwargs['group_chat_created']
        self._supergroup_chat_created = None
        if 'supergroup_chat_created' in kwargs:
            self.supergroup_chat_created = kwargs['supergroup_chat_created']
        self._channel_chat_created = None
        if 'channel_chat_created' in kwargs:
            self.channel_chat_created = kwargs['channel_chat_created']
        self._message_auto_delete_timer_changed = None
        if 'message_auto_delete_timer_changed' in kwargs:
            self.message_auto_delete_timer_changed = kwargs['message_auto_delete_timer_changed']
        self._migrate_to_chat_id = None
        if 'migrate_to_chat_id' in kwargs:
            self.migrate_to_chat_id = kwargs['migrate_to_chat_id']
        self._migrate_from_chat_id = None
        if 'migrate_from_chat_id' in kwargs:
            self.migrate_from_chat_id = kwargs['migrate_from_chat_id']
        self._pinned_message = None
        if 'pinned_message' in kwargs:
            self.pinned_message = kwargs['pinned_message']
        self._invoice = None
        if 'invoice' in kwargs:
            self.invoice = kwargs['invoice']
        self._successful_payment = None
        if 'successful_payment' in kwargs:
            self.successful_payment = kwargs['successful_payment']
        self._refunded_payment = None
        if 'refunded_payment' in kwargs:
            self.refunded_payment = kwargs['refunded_payment']
        self._users_shared = None
        if 'users_shared' in kwargs:
            self.users_shared = kwargs['users_shared']
        self._chat_shared = None
        if 'chat_shared' in kwargs:
            self.chat_shared = kwargs['chat_shared']
        self._connected_website = None
        if 'connected_website' in kwargs:
            self.connected_website = kwargs['connected_website']
        self._write_access_allowed = None
        if 'write_access_allowed' in kwargs:
            self.write_access_allowed = kwargs['write_access_allowed']
        self._passport_data = None
        if 'passport_data' in kwargs:
            self.passport_data = kwargs['passport_data']
        self._proximity_alert_triggered = None
        if 'proximity_alert_triggered' in kwargs:
            self.proximity_alert_triggered = kwargs['proximity_alert_triggered']
        self._boost_added = None
        if 'boost_added' in kwargs:
            self.boost_added = kwargs['boost_added']
        self._chat_background_set = None
        if 'chat_background_set' in kwargs:
            self.chat_background_set = kwargs['chat_background_set']
        self._forum_topic_created = None
        if 'forum_topic_created' in kwargs:
            self.forum_topic_created = kwargs['forum_topic_created']
        self._forum_topic_edited = None
        if 'forum_topic_edited' in kwargs:
            self.forum_topic_edited = kwargs['forum_topic_edited']
        self._forum_topic_closed = None
        if 'forum_topic_closed' in kwargs:
            self.forum_topic_closed = kwargs['forum_topic_closed']
        self._forum_topic_reopened = None
        if 'forum_topic_reopened' in kwargs:
            self.forum_topic_reopened = kwargs['forum_topic_reopened']
        self._general_forum_topic_hidden = None
        if 'general_forum_topic_hidden' in kwargs:
            self.general_forum_topic_hidden = kwargs['general_forum_topic_hidden']
        self._general_forum_topic_unhidden = None
        if 'general_forum_topic_unhidden' in kwargs:
            self.general_forum_topic_unhidden = kwargs['general_forum_topic_unhidden']
        self._giveaway_created = None
        if 'giveaway_created' in kwargs:
            self.giveaway_created = kwargs['giveaway_created']
        self._giveaway = None
        if 'giveaway' in kwargs:
            self.giveaway = kwargs['giveaway']
        self._giveaway_winners = None
        if 'giveaway_winners' in kwargs:
            self.giveaway_winners = kwargs['giveaway_winners']
        self._giveaway_completed = None
        if 'giveaway_completed' in kwargs:
            self.giveaway_completed = kwargs['giveaway_completed']
        self._video_chat_scheduled = None
        if 'video_chat_scheduled' in kwargs:
            self.video_chat_scheduled = kwargs['video_chat_scheduled']
        self._video_chat_started = None
        if 'video_chat_started' in kwargs:
            self.video_chat_started = kwargs['video_chat_started']
        self._video_chat_ended = None
        if 'video_chat_ended' in kwargs:
            self.video_chat_ended = kwargs['video_chat_ended']
        self._video_chat_participants_invited = None
        if 'video_chat_participants_invited' in kwargs:
            self.video_chat_participants_invited = kwargs['video_chat_participants_invited']
        self._web_app_data = None
        if 'web_app_data' in kwargs:
            self.web_app_data = kwargs['web_app_data']
        self._reply_markup = None
        if 'reply_markup' in kwargs:
            self.reply_markup = kwargs['reply_markup']

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    @property
    def message_thread_id(self) -> int | None:
        return self._message_thread_id

    @message_thread_id.setter
    def message_thread_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._message_thread_id = value

    @property
    def from_user(self) -> User | None:
        return self._from_user

    @from_user.setter
    def from_user(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._from_user = value

    @property
    def sender_chat(self) -> Chat | None:
        return self._sender_chat

    @sender_chat.setter
    def sender_chat(self, value: Chat | None) -> None:
        TypeChecker.check(value, 'Chat | None')
        self._sender_chat = value

    @property
    def sender_boost_count(self) -> int | None:
        return self._sender_boost_count

    @sender_boost_count.setter
    def sender_boost_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._sender_boost_count = value

    @property
    def sender_business_bot(self) -> User | None:
        return self._sender_business_bot

    @sender_business_bot.setter
    def sender_business_bot(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._sender_business_bot = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def business_connection_id(self) -> str | None:
        return self._business_connection_id

    @business_connection_id.setter
    def business_connection_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._business_connection_id = value

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def forward_origin(self) -> MessageOrigin | None:
        return self._forward_origin

    @forward_origin.setter
    def forward_origin(self, value: MessageOrigin | None) -> None:
        TypeChecker.check(value, 'MessageOrigin | None')
        self._forward_origin = value

    @property
    def is_topic_message(self) -> bool | None:
        return self._is_topic_message

    @is_topic_message.setter
    def is_topic_message(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_topic_message = value

    @property
    def is_automatic_forward(self) -> bool | None:
        return self._is_automatic_forward

    @is_automatic_forward.setter
    def is_automatic_forward(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_automatic_forward = value

    @property
    def reply_to_message(self) -> Message | None:
        return self._reply_to_message

    @reply_to_message.setter
    def reply_to_message(self, value: Message | None) -> None:
        TypeChecker.check(value, 'Message | None')
        self._reply_to_message = value

    @property
    def external_reply(self) -> ExternalReplyInfo | None:
        return self._external_reply

    @external_reply.setter
    def external_reply(self, value: ExternalReplyInfo | None) -> None:
        TypeChecker.check(value, 'ExternalReplyInfo | None')
        self._external_reply = value

    @property
    def quote(self) -> TextQuote | None:
        return self._quote

    @quote.setter
    def quote(self, value: TextQuote | None) -> None:
        TypeChecker.check(value, 'TextQuote | None')
        self._quote = value

    @property
    def reply_to_story(self) -> Story | None:
        return self._reply_to_story

    @reply_to_story.setter
    def reply_to_story(self, value: Story | None) -> None:
        TypeChecker.check(value, 'Story | None')
        self._reply_to_story = value

    @property
    def via_bot(self) -> User | None:
        return self._via_bot

    @via_bot.setter
    def via_bot(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._via_bot = value

    @property
    def edit_date(self) -> int | None:
        return self._edit_date

    @edit_date.setter
    def edit_date(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._edit_date = value

    @property
    def has_protected_content(self) -> bool | None:
        return self._has_protected_content

    @has_protected_content.setter
    def has_protected_content(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_protected_content = value

    @property
    def is_from_offline(self) -> bool | None:
        return self._is_from_offline

    @is_from_offline.setter
    def is_from_offline(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_from_offline = value

    @property
    def media_group_id(self) -> str | None:
        return self._media_group_id

    @media_group_id.setter
    def media_group_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._media_group_id = value

    @property
    def author_signature(self) -> str | None:
        return self._author_signature

    @author_signature.setter
    def author_signature(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._author_signature = value

    @property
    def text(self) -> str | None:
        return self._text

    @text.setter
    def text(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._text = value

    @property
    def entities(self) -> List[MessageEntity] | None:
        return self._entities

    @entities.setter
    def entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._entities = value

    @property
    def link_preview_options(self) -> LinkPreviewOptions | None:
        return self._link_preview_options

    @link_preview_options.setter
    def link_preview_options(self, value: LinkPreviewOptions | None) -> None:
        TypeChecker.check(value, 'LinkPreviewOptions | None')
        self._link_preview_options = value

    @property
    def effect_id(self) -> str | None:
        return self._effect_id

    @effect_id.setter
    def effect_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._effect_id = value

    @property
    def animation(self) -> Animation | None:
        return self._animation

    @animation.setter
    def animation(self, value: Animation | None) -> None:
        TypeChecker.check(value, 'Animation | None')
        self._animation = value

    @property
    def audio(self) -> Audio | None:
        return self._audio

    @audio.setter
    def audio(self, value: Audio | None) -> None:
        TypeChecker.check(value, 'Audio | None')
        self._audio = value

    @property
    def document(self) -> Document | None:
        return self._document

    @document.setter
    def document(self, value: Document | None) -> None:
        TypeChecker.check(value, 'Document | None')
        self._document = value

    @property
    def paid_media(self) -> PaidMediaInfo | None:
        return self._paid_media

    @paid_media.setter
    def paid_media(self, value: PaidMediaInfo | None) -> None:
        TypeChecker.check(value, 'PaidMediaInfo | None')
        self._paid_media = value

    @property
    def photo(self) -> List[PhotoSize] | None:
        return self._photo

    @photo.setter
    def photo(self, value: List[PhotoSize] | None) -> None:
        TypeChecker.check(value, 'List[PhotoSize] | None')
        self._photo = value

    @property
    def sticker(self) -> Sticker | None:
        return self._sticker

    @sticker.setter
    def sticker(self, value: Sticker | None) -> None:
        TypeChecker.check(value, 'Sticker | None')
        self._sticker = value

    @property
    def story(self) -> Story | None:
        return self._story

    @story.setter
    def story(self, value: Story | None) -> None:
        TypeChecker.check(value, 'Story | None')
        self._story = value

    @property
    def video(self) -> Video | None:
        return self._video

    @video.setter
    def video(self, value: Video | None) -> None:
        TypeChecker.check(value, 'Video | None')
        self._video = value

    @property
    def video_note(self) -> VideoNote | None:
        return self._video_note

    @video_note.setter
    def video_note(self, value: VideoNote | None) -> None:
        TypeChecker.check(value, 'VideoNote | None')
        self._video_note = value

    @property
    def voice(self) -> Voice | None:
        return self._voice

    @voice.setter
    def voice(self, value: Voice | None) -> None:
        TypeChecker.check(value, 'Voice | None')
        self._voice = value

    @property
    def caption(self) -> str | None:
        return self._caption

    @caption.setter
    def caption(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._caption = value

    @property
    def caption_entities(self) -> List[MessageEntity] | None:
        return self._caption_entities

    @caption_entities.setter
    def caption_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._caption_entities = value

    @property
    def show_caption_above_media(self) -> bool | None:
        return self._show_caption_above_media

    @show_caption_above_media.setter
    def show_caption_above_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._show_caption_above_media = value

    @property
    def has_media_spoiler(self) -> bool | None:
        return self._has_media_spoiler

    @has_media_spoiler.setter
    def has_media_spoiler(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_media_spoiler = value

    @property
    def contact(self) -> Contact | None:
        return self._contact

    @contact.setter
    def contact(self, value: Contact | None) -> None:
        TypeChecker.check(value, 'Contact | None')
        self._contact = value

    @property
    def dice(self) -> Dice | None:
        return self._dice

    @dice.setter
    def dice(self, value: Dice | None) -> None:
        TypeChecker.check(value, 'Dice | None')
        self._dice = value

    @property
    def game(self) -> Game | None:
        return self._game

    @game.setter
    def game(self, value: Game | None) -> None:
        TypeChecker.check(value, 'Game | None')
        self._game = value

    @property
    def poll(self) -> Poll | None:
        return self._poll

    @poll.setter
    def poll(self, value: Poll | None) -> None:
        TypeChecker.check(value, 'Poll | None')
        self._poll = value

    @property
    def venue(self) -> Venue | None:
        return self._venue

    @venue.setter
    def venue(self, value: Venue | None) -> None:
        TypeChecker.check(value, 'Venue | None')
        self._venue = value

    @property
    def location(self) -> Location | None:
        return self._location

    @location.setter
    def location(self, value: Location | None) -> None:
        TypeChecker.check(value, 'Location | None')
        self._location = value

    @property
    def new_chat_members(self) -> List[User] | None:
        return self._new_chat_members

    @new_chat_members.setter
    def new_chat_members(self, value: List[User] | None) -> None:
        TypeChecker.check(value, 'List[User] | None')
        self._new_chat_members = value

    @property
    def left_chat_member(self) -> User | None:
        return self._left_chat_member

    @left_chat_member.setter
    def left_chat_member(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._left_chat_member = value

    @property
    def new_chat_title(self) -> str | None:
        return self._new_chat_title

    @new_chat_title.setter
    def new_chat_title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._new_chat_title = value

    @property
    def new_chat_photo(self) -> List[PhotoSize] | None:
        return self._new_chat_photo

    @new_chat_photo.setter
    def new_chat_photo(self, value: List[PhotoSize] | None) -> None:
        TypeChecker.check(value, 'List[PhotoSize] | None')
        self._new_chat_photo = value

    @property
    def delete_chat_photo(self) -> bool | None:
        return self._delete_chat_photo

    @delete_chat_photo.setter
    def delete_chat_photo(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._delete_chat_photo = value

    @property
    def group_chat_created(self) -> bool | None:
        return self._group_chat_created

    @group_chat_created.setter
    def group_chat_created(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._group_chat_created = value

    @property
    def supergroup_chat_created(self) -> bool | None:
        return self._supergroup_chat_created

    @supergroup_chat_created.setter
    def supergroup_chat_created(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._supergroup_chat_created = value

    @property
    def channel_chat_created(self) -> bool | None:
        return self._channel_chat_created

    @channel_chat_created.setter
    def channel_chat_created(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._channel_chat_created = value

    @property
    def message_auto_delete_timer_changed(self) -> MessageAutoDeleteTimerChanged | None:
        return self._message_auto_delete_timer_changed

    @message_auto_delete_timer_changed.setter
    def message_auto_delete_timer_changed(self, value: MessageAutoDeleteTimerChanged | None) -> None:
        TypeChecker.check(value, 'MessageAutoDeleteTimerChanged | None')
        self._message_auto_delete_timer_changed = value

    @property
    def migrate_to_chat_id(self) -> int | None:
        return self._migrate_to_chat_id

    @migrate_to_chat_id.setter
    def migrate_to_chat_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._migrate_to_chat_id = value

    @property
    def migrate_from_chat_id(self) -> int | None:
        return self._migrate_from_chat_id

    @migrate_from_chat_id.setter
    def migrate_from_chat_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._migrate_from_chat_id = value

    @property
    def pinned_message(self) -> MaybeInaccessibleMessage | None:
        return self._pinned_message

    @pinned_message.setter
    def pinned_message(self, value: MaybeInaccessibleMessage | None) -> None:
        TypeChecker.check(value, 'MaybeInaccessibleMessage | None')
        self._pinned_message = value

    @property
    def invoice(self) -> Invoice | None:
        return self._invoice

    @invoice.setter
    def invoice(self, value: Invoice | None) -> None:
        TypeChecker.check(value, 'Invoice | None')
        self._invoice = value

    @property
    def successful_payment(self) -> SuccessfulPayment | None:
        return self._successful_payment

    @successful_payment.setter
    def successful_payment(self, value: SuccessfulPayment | None) -> None:
        TypeChecker.check(value, 'SuccessfulPayment | None')
        self._successful_payment = value

    @property
    def refunded_payment(self) -> RefundedPayment | None:
        return self._refunded_payment

    @refunded_payment.setter
    def refunded_payment(self, value: RefundedPayment | None) -> None:
        TypeChecker.check(value, 'RefundedPayment | None')
        self._refunded_payment = value

    @property
    def users_shared(self) -> UsersShared | None:
        return self._users_shared

    @users_shared.setter
    def users_shared(self, value: UsersShared | None) -> None:
        TypeChecker.check(value, 'UsersShared | None')
        self._users_shared = value

    @property
    def chat_shared(self) -> ChatShared | None:
        return self._chat_shared

    @chat_shared.setter
    def chat_shared(self, value: ChatShared | None) -> None:
        TypeChecker.check(value, 'ChatShared | None')
        self._chat_shared = value

    @property
    def connected_website(self) -> str | None:
        return self._connected_website

    @connected_website.setter
    def connected_website(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._connected_website = value

    @property
    def write_access_allowed(self) -> WriteAccessAllowed | None:
        return self._write_access_allowed

    @write_access_allowed.setter
    def write_access_allowed(self, value: WriteAccessAllowed | None) -> None:
        TypeChecker.check(value, 'WriteAccessAllowed | None')
        self._write_access_allowed = value

    @property
    def passport_data(self) -> PassportData | None:
        return self._passport_data

    @passport_data.setter
    def passport_data(self, value: PassportData | None) -> None:
        TypeChecker.check(value, 'PassportData | None')
        self._passport_data = value

    @property
    def proximity_alert_triggered(self) -> ProximityAlertTriggered | None:
        return self._proximity_alert_triggered

    @proximity_alert_triggered.setter
    def proximity_alert_triggered(self, value: ProximityAlertTriggered | None) -> None:
        TypeChecker.check(value, 'ProximityAlertTriggered | None')
        self._proximity_alert_triggered = value

    @property
    def boost_added(self) -> ChatBoostAdded | None:
        return self._boost_added

    @boost_added.setter
    def boost_added(self, value: ChatBoostAdded | None) -> None:
        TypeChecker.check(value, 'ChatBoostAdded | None')
        self._boost_added = value

    @property
    def chat_background_set(self) -> ChatBackground | None:
        return self._chat_background_set

    @chat_background_set.setter
    def chat_background_set(self, value: ChatBackground | None) -> None:
        TypeChecker.check(value, 'ChatBackground | None')
        self._chat_background_set = value

    @property
    def forum_topic_created(self) -> ForumTopicCreated | None:
        return self._forum_topic_created

    @forum_topic_created.setter
    def forum_topic_created(self, value: ForumTopicCreated | None) -> None:
        TypeChecker.check(value, 'ForumTopicCreated | None')
        self._forum_topic_created = value

    @property
    def forum_topic_edited(self) -> ForumTopicEdited | None:
        return self._forum_topic_edited

    @forum_topic_edited.setter
    def forum_topic_edited(self, value: ForumTopicEdited | None) -> None:
        TypeChecker.check(value, 'ForumTopicEdited | None')
        self._forum_topic_edited = value

    @property
    def forum_topic_closed(self) -> ForumTopicClosed | None:
        return self._forum_topic_closed

    @forum_topic_closed.setter
    def forum_topic_closed(self, value: ForumTopicClosed | None) -> None:
        TypeChecker.check(value, 'ForumTopicClosed | None')
        self._forum_topic_closed = value

    @property
    def forum_topic_reopened(self) -> ForumTopicReopened | None:
        return self._forum_topic_reopened

    @forum_topic_reopened.setter
    def forum_topic_reopened(self, value: ForumTopicReopened | None) -> None:
        TypeChecker.check(value, 'ForumTopicReopened | None')
        self._forum_topic_reopened = value

    @property
    def general_forum_topic_hidden(self) -> GeneralForumTopicHidden | None:
        return self._general_forum_topic_hidden

    @general_forum_topic_hidden.setter
    def general_forum_topic_hidden(self, value: GeneralForumTopicHidden | None) -> None:
        TypeChecker.check(value, 'GeneralForumTopicHidden | None')
        self._general_forum_topic_hidden = value

    @property
    def general_forum_topic_unhidden(self) -> GeneralForumTopicUnhidden | None:
        return self._general_forum_topic_unhidden

    @general_forum_topic_unhidden.setter
    def general_forum_topic_unhidden(self, value: GeneralForumTopicUnhidden | None) -> None:
        TypeChecker.check(value, 'GeneralForumTopicUnhidden | None')
        self._general_forum_topic_unhidden = value

    @property
    def giveaway_created(self) -> GiveawayCreated | None:
        return self._giveaway_created

    @giveaway_created.setter
    def giveaway_created(self, value: GiveawayCreated | None) -> None:
        TypeChecker.check(value, 'GiveawayCreated | None')
        self._giveaway_created = value

    @property
    def giveaway(self) -> Giveaway | None:
        return self._giveaway

    @giveaway.setter
    def giveaway(self, value: Giveaway | None) -> None:
        TypeChecker.check(value, 'Giveaway | None')
        self._giveaway = value

    @property
    def giveaway_winners(self) -> GiveawayWinners | None:
        return self._giveaway_winners

    @giveaway_winners.setter
    def giveaway_winners(self, value: GiveawayWinners | None) -> None:
        TypeChecker.check(value, 'GiveawayWinners | None')
        self._giveaway_winners = value

    @property
    def giveaway_completed(self) -> GiveawayCompleted | None:
        return self._giveaway_completed

    @giveaway_completed.setter
    def giveaway_completed(self, value: GiveawayCompleted | None) -> None:
        TypeChecker.check(value, 'GiveawayCompleted | None')
        self._giveaway_completed = value

    @property
    def video_chat_scheduled(self) -> VideoChatScheduled | None:
        return self._video_chat_scheduled

    @video_chat_scheduled.setter
    def video_chat_scheduled(self, value: VideoChatScheduled | None) -> None:
        TypeChecker.check(value, 'VideoChatScheduled | None')
        self._video_chat_scheduled = value

    @property
    def video_chat_started(self) -> VideoChatStarted | None:
        return self._video_chat_started

    @video_chat_started.setter
    def video_chat_started(self, value: VideoChatStarted | None) -> None:
        TypeChecker.check(value, 'VideoChatStarted | None')
        self._video_chat_started = value

    @property
    def video_chat_ended(self) -> VideoChatEnded | None:
        return self._video_chat_ended

    @video_chat_ended.setter
    def video_chat_ended(self, value: VideoChatEnded | None) -> None:
        TypeChecker.check(value, 'VideoChatEnded | None')
        self._video_chat_ended = value

    @property
    def video_chat_participants_invited(self) -> VideoChatParticipantsInvited | None:
        return self._video_chat_participants_invited

    @video_chat_participants_invited.setter
    def video_chat_participants_invited(self, value: VideoChatParticipantsInvited | None) -> None:
        TypeChecker.check(value, 'VideoChatParticipantsInvited | None')
        self._video_chat_participants_invited = value

    @property
    def web_app_data(self) -> WebAppData | None:
        return self._web_app_data

    @web_app_data.setter
    def web_app_data(self, value: WebAppData | None) -> None:
        TypeChecker.check(value, 'WebAppData | None')
        self._web_app_data = value

    @property
    def reply_markup(self) -> InlineKeyboardMarkup | None:
        return self._reply_markup

    @reply_markup.setter
    def reply_markup(self, value: InlineKeyboardMarkup | None) -> None:
        TypeChecker.check(value, 'InlineKeyboardMarkup | None')
        self._reply_markup = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'message_id': self._message_id,
            'message_thread_id': self._message_thread_id,
            'from_user': self._from_user,
            'sender_chat': self._sender_chat,
            'sender_boost_count': self._sender_boost_count,
            'sender_business_bot': self._sender_business_bot,
            'date': self._date,
            'business_connection_id': self._business_connection_id,
            'chat': self._chat,
            'forward_origin': self._forward_origin,
            'is_topic_message': self._is_topic_message,
            'is_automatic_forward': self._is_automatic_forward,
            'reply_to_message': self._reply_to_message,
            'external_reply': self._external_reply,
            'quote': self._quote,
            'reply_to_story': self._reply_to_story,
            'via_bot': self._via_bot,
            'edit_date': self._edit_date,
            'has_protected_content': self._has_protected_content,
            'is_from_offline': self._is_from_offline,
            'media_group_id': self._media_group_id,
            'author_signature': self._author_signature,
            'text': self._text,
            'entities': self._entities,
            'link_preview_options': self._link_preview_options,
            'effect_id': self._effect_id,
            'animation': self._animation,
            'audio': self._audio,
            'document': self._document,
            'paid_media': self._paid_media,
            'photo': self._photo,
            'sticker': self._sticker,
            'story': self._story,
            'video': self._video,
            'video_note': self._video_note,
            'voice': self._voice,
            'caption': self._caption,
            'caption_entities': self._caption_entities,
            'show_caption_above_media': self._show_caption_above_media,
            'has_media_spoiler': self._has_media_spoiler,
            'contact': self._contact,
            'dice': self._dice,
            'game': self._game,
            'poll': self._poll,
            'venue': self._venue,
            'location': self._location,
            'new_chat_members': self._new_chat_members,
            'left_chat_member': self._left_chat_member,
            'new_chat_title': self._new_chat_title,
            'new_chat_photo': self._new_chat_photo,
            'delete_chat_photo': self._delete_chat_photo,
            'group_chat_created': self._group_chat_created,
            'supergroup_chat_created': self._supergroup_chat_created,
            'channel_chat_created': self._channel_chat_created,
            'message_auto_delete_timer_changed': self._message_auto_delete_timer_changed,
            'migrate_to_chat_id': self._migrate_to_chat_id,
            'migrate_from_chat_id': self._migrate_from_chat_id,
            'pinned_message': self._pinned_message,
            'invoice': self._invoice,
            'successful_payment': self._successful_payment,
            'refunded_payment': self._refunded_payment,
            'users_shared': self._users_shared,
            'chat_shared': self._chat_shared,
            'connected_website': self._connected_website,
            'write_access_allowed': self._write_access_allowed,
            'passport_data': self._passport_data,
            'proximity_alert_triggered': self._proximity_alert_triggered,
            'boost_added': self._boost_added,
            'chat_background_set': self._chat_background_set,
            'forum_topic_created': self._forum_topic_created,
            'forum_topic_edited': self._forum_topic_edited,
            'forum_topic_closed': self._forum_topic_closed,
            'forum_topic_reopened': self._forum_topic_reopened,
            'general_forum_topic_hidden': self._general_forum_topic_hidden,
            'general_forum_topic_unhidden': self._general_forum_topic_unhidden,
            'giveaway_created': self._giveaway_created,
            'giveaway': self._giveaway,
            'giveaway_winners': self._giveaway_winners,
            'giveaway_completed': self._giveaway_completed,
            'video_chat_scheduled': self._video_chat_scheduled,
            'video_chat_started': self._video_chat_started,
            'video_chat_ended': self._video_chat_ended,
            'video_chat_participants_invited': self._video_chat_participants_invited,
            'web_app_data': self._web_app_data,
            'reply_markup': self._reply_markup,
        }

class MessageId:
    """This object represents a unique message identifier."""
    def __init__(self, **kwargs: Any):
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'message_id': self._message_id,
        }

class InaccessibleMessage:
    """This object describes a message that was deleted or is otherwise inaccessible to the bot."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'message_id': self._message_id,
            'date': self._date,
        }

class MaybeInaccessibleMessage:
    """This object describes a message that can be inaccessible to the bot. It can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._offset = None
        if 'offset' in kwargs:
            self.offset = kwargs['offset']
        self._length = None
        if 'length' in kwargs:
            self.length = kwargs['length']
        self._url = None
        if 'url' in kwargs:
            self.url = kwargs['url']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._language = None
        if 'language' in kwargs:
            self.language = kwargs['language']
        self._custom_emoji_id = None
        if 'custom_emoji_id' in kwargs:
            self.custom_emoji_id = kwargs['custom_emoji_id']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def offset(self) -> int:
        return self._offset

    @offset.setter
    def offset(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._offset = value

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._length = value

    @property
    def url(self) -> str | None:
        return self._url

    @url.setter
    def url(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._url = value

    @property
    def user(self) -> User | None:
        return self._user

    @user.setter
    def user(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._user = value

    @property
    def language(self) -> str | None:
        return self._language

    @language.setter
    def language(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._language = value

    @property
    def custom_emoji_id(self) -> str | None:
        return self._custom_emoji_id

    @custom_emoji_id.setter
    def custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._custom_emoji_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'offset': self._offset,
            'length': self._length,
            'url': self._url,
            'user': self._user,
            'language': self._language,
            'custom_emoji_id': self._custom_emoji_id,
        }

class TextQuote:
    """This object contains information about the quoted part of a message that is replied to by the given message."""
    def __init__(self, **kwargs: Any):
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._entities = None
        if 'entities' in kwargs:
            self.entities = kwargs['entities']
        self._position = None
        if 'position' in kwargs:
            self.position = kwargs['position']
        self._is_manual = None
        if 'is_manual' in kwargs:
            self.is_manual = kwargs['is_manual']

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._text = value

    @property
    def entities(self) -> List[MessageEntity] | None:
        return self._entities

    @entities.setter
    def entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._entities = value

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._position = value

    @property
    def is_manual(self) -> bool | None:
        return self._is_manual

    @is_manual.setter
    def is_manual(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_manual = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'text': self._text,
            'entities': self._entities,
            'position': self._position,
            'is_manual': self._is_manual,
        }

class ExternalReplyInfo:
    """This object contains information about a message that is being replied to, which may come from another chat or forum topic."""
    def __init__(self, **kwargs: Any):
        self._origin = None
        if 'origin' in kwargs:
            self.origin = kwargs['origin']
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._link_preview_options = None
        if 'link_preview_options' in kwargs:
            self.link_preview_options = kwargs['link_preview_options']
        self._animation = None
        if 'animation' in kwargs:
            self.animation = kwargs['animation']
        self._audio = None
        if 'audio' in kwargs:
            self.audio = kwargs['audio']
        self._document = None
        if 'document' in kwargs:
            self.document = kwargs['document']
        self._paid_media = None
        if 'paid_media' in kwargs:
            self.paid_media = kwargs['paid_media']
        self._photo = None
        if 'photo' in kwargs:
            self.photo = kwargs['photo']
        self._sticker = None
        if 'sticker' in kwargs:
            self.sticker = kwargs['sticker']
        self._story = None
        if 'story' in kwargs:
            self.story = kwargs['story']
        self._video = None
        if 'video' in kwargs:
            self.video = kwargs['video']
        self._video_note = None
        if 'video_note' in kwargs:
            self.video_note = kwargs['video_note']
        self._voice = None
        if 'voice' in kwargs:
            self.voice = kwargs['voice']
        self._has_media_spoiler = None
        if 'has_media_spoiler' in kwargs:
            self.has_media_spoiler = kwargs['has_media_spoiler']
        self._contact = None
        if 'contact' in kwargs:
            self.contact = kwargs['contact']
        self._dice = None
        if 'dice' in kwargs:
            self.dice = kwargs['dice']
        self._game = None
        if 'game' in kwargs:
            self.game = kwargs['game']
        self._giveaway = None
        if 'giveaway' in kwargs:
            self.giveaway = kwargs['giveaway']
        self._giveaway_winners = None
        if 'giveaway_winners' in kwargs:
            self.giveaway_winners = kwargs['giveaway_winners']
        self._invoice = None
        if 'invoice' in kwargs:
            self.invoice = kwargs['invoice']
        self._location = None
        if 'location' in kwargs:
            self.location = kwargs['location']
        self._poll = None
        if 'poll' in kwargs:
            self.poll = kwargs['poll']
        self._venue = None
        if 'venue' in kwargs:
            self.venue = kwargs['venue']

    @property
    def origin(self) -> MessageOrigin:
        return self._origin

    @origin.setter
    def origin(self, value: MessageOrigin) -> None:
        TypeChecker.check(value, 'MessageOrigin')
        self._origin = value

    @property
    def chat(self) -> Chat | None:
        return self._chat

    @chat.setter
    def chat(self, value: Chat | None) -> None:
        TypeChecker.check(value, 'Chat | None')
        self._chat = value

    @property
    def message_id(self) -> int | None:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._message_id = value

    @property
    def link_preview_options(self) -> LinkPreviewOptions | None:
        return self._link_preview_options

    @link_preview_options.setter
    def link_preview_options(self, value: LinkPreviewOptions | None) -> None:
        TypeChecker.check(value, 'LinkPreviewOptions | None')
        self._link_preview_options = value

    @property
    def animation(self) -> Animation | None:
        return self._animation

    @animation.setter
    def animation(self, value: Animation | None) -> None:
        TypeChecker.check(value, 'Animation | None')
        self._animation = value

    @property
    def audio(self) -> Audio | None:
        return self._audio

    @audio.setter
    def audio(self, value: Audio | None) -> None:
        TypeChecker.check(value, 'Audio | None')
        self._audio = value

    @property
    def document(self) -> Document | None:
        return self._document

    @document.setter
    def document(self, value: Document | None) -> None:
        TypeChecker.check(value, 'Document | None')
        self._document = value

    @property
    def paid_media(self) -> PaidMediaInfo | None:
        return self._paid_media

    @paid_media.setter
    def paid_media(self, value: PaidMediaInfo | None) -> None:
        TypeChecker.check(value, 'PaidMediaInfo | None')
        self._paid_media = value

    @property
    def photo(self) -> List[PhotoSize] | None:
        return self._photo

    @photo.setter
    def photo(self, value: List[PhotoSize] | None) -> None:
        TypeChecker.check(value, 'List[PhotoSize] | None')
        self._photo = value

    @property
    def sticker(self) -> Sticker | None:
        return self._sticker

    @sticker.setter
    def sticker(self, value: Sticker | None) -> None:
        TypeChecker.check(value, 'Sticker | None')
        self._sticker = value

    @property
    def story(self) -> Story | None:
        return self._story

    @story.setter
    def story(self, value: Story | None) -> None:
        TypeChecker.check(value, 'Story | None')
        self._story = value

    @property
    def video(self) -> Video | None:
        return self._video

    @video.setter
    def video(self, value: Video | None) -> None:
        TypeChecker.check(value, 'Video | None')
        self._video = value

    @property
    def video_note(self) -> VideoNote | None:
        return self._video_note

    @video_note.setter
    def video_note(self, value: VideoNote | None) -> None:
        TypeChecker.check(value, 'VideoNote | None')
        self._video_note = value

    @property
    def voice(self) -> Voice | None:
        return self._voice

    @voice.setter
    def voice(self, value: Voice | None) -> None:
        TypeChecker.check(value, 'Voice | None')
        self._voice = value

    @property
    def has_media_spoiler(self) -> bool | None:
        return self._has_media_spoiler

    @has_media_spoiler.setter
    def has_media_spoiler(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_media_spoiler = value

    @property
    def contact(self) -> Contact | None:
        return self._contact

    @contact.setter
    def contact(self, value: Contact | None) -> None:
        TypeChecker.check(value, 'Contact | None')
        self._contact = value

    @property
    def dice(self) -> Dice | None:
        return self._dice

    @dice.setter
    def dice(self, value: Dice | None) -> None:
        TypeChecker.check(value, 'Dice | None')
        self._dice = value

    @property
    def game(self) -> Game | None:
        return self._game

    @game.setter
    def game(self, value: Game | None) -> None:
        TypeChecker.check(value, 'Game | None')
        self._game = value

    @property
    def giveaway(self) -> Giveaway | None:
        return self._giveaway

    @giveaway.setter
    def giveaway(self, value: Giveaway | None) -> None:
        TypeChecker.check(value, 'Giveaway | None')
        self._giveaway = value

    @property
    def giveaway_winners(self) -> GiveawayWinners | None:
        return self._giveaway_winners

    @giveaway_winners.setter
    def giveaway_winners(self, value: GiveawayWinners | None) -> None:
        TypeChecker.check(value, 'GiveawayWinners | None')
        self._giveaway_winners = value

    @property
    def invoice(self) -> Invoice | None:
        return self._invoice

    @invoice.setter
    def invoice(self, value: Invoice | None) -> None:
        TypeChecker.check(value, 'Invoice | None')
        self._invoice = value

    @property
    def location(self) -> Location | None:
        return self._location

    @location.setter
    def location(self, value: Location | None) -> None:
        TypeChecker.check(value, 'Location | None')
        self._location = value

    @property
    def poll(self) -> Poll | None:
        return self._poll

    @poll.setter
    def poll(self, value: Poll | None) -> None:
        TypeChecker.check(value, 'Poll | None')
        self._poll = value

    @property
    def venue(self) -> Venue | None:
        return self._venue

    @venue.setter
    def venue(self, value: Venue | None) -> None:
        TypeChecker.check(value, 'Venue | None')
        self._venue = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'origin': self._origin,
            'chat': self._chat,
            'message_id': self._message_id,
            'link_preview_options': self._link_preview_options,
            'animation': self._animation,
            'audio': self._audio,
            'document': self._document,
            'paid_media': self._paid_media,
            'photo': self._photo,
            'sticker': self._sticker,
            'story': self._story,
            'video': self._video,
            'video_note': self._video_note,
            'voice': self._voice,
            'has_media_spoiler': self._has_media_spoiler,
            'contact': self._contact,
            'dice': self._dice,
            'game': self._game,
            'giveaway': self._giveaway,
            'giveaway_winners': self._giveaway_winners,
            'invoice': self._invoice,
            'location': self._location,
            'poll': self._poll,
            'venue': self._venue,
        }

class ReplyParameters:
    """Describes reply parameters for the message that is being sent."""
    def __init__(self, **kwargs: Any):
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._chat_id = None
        if 'chat_id' in kwargs:
            self.chat_id = kwargs['chat_id']
        self._allow_sending_without_reply = None
        if 'allow_sending_without_reply' in kwargs:
            self.allow_sending_without_reply = kwargs['allow_sending_without_reply']
        self._quote = None
        if 'quote' in kwargs:
            self.quote = kwargs['quote']
        self._quote_parse_mode = None
        if 'quote_parse_mode' in kwargs:
            self.quote_parse_mode = kwargs['quote_parse_mode']
        self._quote_entities = None
        if 'quote_entities' in kwargs:
            self.quote_entities = kwargs['quote_entities']
        self._quote_position = None
        if 'quote_position' in kwargs:
            self.quote_position = kwargs['quote_position']

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    @property
    def chat_id(self) -> int | str | None:
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value: int | str | None) -> None:
        TypeChecker.check(value, 'int | str | None')
        self._chat_id = value

    @property
    def allow_sending_without_reply(self) -> bool | None:
        return self._allow_sending_without_reply

    @allow_sending_without_reply.setter
    def allow_sending_without_reply(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._allow_sending_without_reply = value

    @property
    def quote(self) -> str | None:
        return self._quote

    @quote.setter
    def quote(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._quote = value

    @property
    def quote_parse_mode(self) -> str | None:
        return self._quote_parse_mode

    @quote_parse_mode.setter
    def quote_parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._quote_parse_mode = value

    @property
    def quote_entities(self) -> List[MessageEntity] | None:
        return self._quote_entities

    @quote_entities.setter
    def quote_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._quote_entities = value

    @property
    def quote_position(self) -> int | None:
        return self._quote_position

    @quote_position.setter
    def quote_position(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._quote_position = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'message_id': self._message_id,
            'chat_id': self._chat_id,
            'allow_sending_without_reply': self._allow_sending_without_reply,
            'quote': self._quote,
            'quote_parse_mode': self._quote_parse_mode,
            'quote_entities': self._quote_entities,
            'quote_position': self._quote_position,
        }

class MessageOrigin:
    """This object describes the origin of a message. It can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class MessageOriginUser:
    """The message was originally sent by a known user."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._sender_user = None
        if 'sender_user' in kwargs:
            self.sender_user = kwargs['sender_user']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def sender_user(self) -> User:
        return self._sender_user

    @sender_user.setter
    def sender_user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._sender_user = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'date': self._date,
            'sender_user': self._sender_user,
        }

class MessageOriginHiddenUser:
    """The message was originally sent by an unknown user."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._sender_user_name = None
        if 'sender_user_name' in kwargs:
            self.sender_user_name = kwargs['sender_user_name']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def sender_user_name(self) -> str:
        return self._sender_user_name

    @sender_user_name.setter
    def sender_user_name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._sender_user_name = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'date': self._date,
            'sender_user_name': self._sender_user_name,
        }

class MessageOriginChat:
    """The message was originally sent on behalf of a chat to a group chat."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._sender_chat = None
        if 'sender_chat' in kwargs:
            self.sender_chat = kwargs['sender_chat']
        self._author_signature = None
        if 'author_signature' in kwargs:
            self.author_signature = kwargs['author_signature']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def sender_chat(self) -> Chat:
        return self._sender_chat

    @sender_chat.setter
    def sender_chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._sender_chat = value

    @property
    def author_signature(self) -> str | None:
        return self._author_signature

    @author_signature.setter
    def author_signature(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._author_signature = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'date': self._date,
            'sender_chat': self._sender_chat,
            'author_signature': self._author_signature,
        }

class MessageOriginChannel:
    """The message was originally sent to a channel chat."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._author_signature = None
        if 'author_signature' in kwargs:
            self.author_signature = kwargs['author_signature']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    @property
    def author_signature(self) -> str | None:
        return self._author_signature

    @author_signature.setter
    def author_signature(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._author_signature = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'date': self._date,
            'chat': self._chat,
            'message_id': self._message_id,
            'author_signature': self._author_signature,
        }

class PhotoSize:
    """This object represents one size of a photo or a file / sticker thumbnail."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._height = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'width': self._width,
            'height': self._height,
            'file_size': self._file_size,
        }

class Animation:
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound)."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._file_name = None
        if 'file_name' in kwargs:
            self.file_name = kwargs['file_name']
        self._mime_type = None
        if 'mime_type' in kwargs:
            self.mime_type = kwargs['mime_type']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._height = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._duration = value

    @property
    def thumbnail(self) -> PhotoSize | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: PhotoSize | None) -> None:
        TypeChecker.check(value, 'PhotoSize | None')
        self._thumbnail = value

    @property
    def file_name(self) -> str | None:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._file_name = value

    @property
    def mime_type(self) -> str | None:
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._mime_type = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'width': self._width,
            'height': self._height,
            'duration': self._duration,
            'thumbnail': self._thumbnail,
            'file_name': self._file_name,
            'mime_type': self._mime_type,
            'file_size': self._file_size,
        }

class Audio:
    """This object represents an audio file to be treated as music by the Telegram clients."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._performer = None
        if 'performer' in kwargs:
            self.performer = kwargs['performer']
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']
        self._file_name = None
        if 'file_name' in kwargs:
            self.file_name = kwargs['file_name']
        self._mime_type = None
        if 'mime_type' in kwargs:
            self.mime_type = kwargs['mime_type']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._duration = value

    @property
    def performer(self) -> str | None:
        return self._performer

    @performer.setter
    def performer(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._performer = value

    @property
    def title(self) -> str | None:
        return self._title

    @title.setter
    def title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._title = value

    @property
    def file_name(self) -> str | None:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._file_name = value

    @property
    def mime_type(self) -> str | None:
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._mime_type = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    @property
    def thumbnail(self) -> PhotoSize | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: PhotoSize | None) -> None:
        TypeChecker.check(value, 'PhotoSize | None')
        self._thumbnail = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'duration': self._duration,
            'performer': self._performer,
            'title': self._title,
            'file_name': self._file_name,
            'mime_type': self._mime_type,
            'file_size': self._file_size,
            'thumbnail': self._thumbnail,
        }

class Document:
    """This object represents a general file (as opposed to photos, voice messages and audio files)."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._file_name = None
        if 'file_name' in kwargs:
            self.file_name = kwargs['file_name']
        self._mime_type = None
        if 'mime_type' in kwargs:
            self.mime_type = kwargs['mime_type']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def thumbnail(self) -> PhotoSize | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: PhotoSize | None) -> None:
        TypeChecker.check(value, 'PhotoSize | None')
        self._thumbnail = value

    @property
    def file_name(self) -> str | None:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._file_name = value

    @property
    def mime_type(self) -> str | None:
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._mime_type = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'thumbnail': self._thumbnail,
            'file_name': self._file_name,
            'mime_type': self._mime_type,
            'file_size': self._file_size,
        }

class Story:
    """This object represents a story."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'id': self._id,
        }

class Video:
    """This object represents a video file."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._cover = None
        if 'cover' in kwargs:
            self.cover = kwargs['cover']
        self._start_timestamp = None
        if 'start_timestamp' in kwargs:
            self.start_timestamp = kwargs['start_timestamp']
        self._file_name = None
        if 'file_name' in kwargs:
            self.file_name = kwargs['file_name']
        self._mime_type = None
        if 'mime_type' in kwargs:
            self.mime_type = kwargs['mime_type']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._height = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._duration = value

    @property
    def thumbnail(self) -> PhotoSize | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: PhotoSize | None) -> None:
        TypeChecker.check(value, 'PhotoSize | None')
        self._thumbnail = value

    @property
    def cover(self) -> List[PhotoSize] | None:
        return self._cover

    @cover.setter
    def cover(self, value: List[PhotoSize] | None) -> None:
        TypeChecker.check(value, 'List[PhotoSize] | None')
        self._cover = value

    @property
    def start_timestamp(self) -> int | None:
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._start_timestamp = value

    @property
    def file_name(self) -> str | None:
        return self._file_name

    @file_name.setter
    def file_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._file_name = value

    @property
    def mime_type(self) -> str | None:
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._mime_type = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'width': self._width,
            'height': self._height,
            'duration': self._duration,
            'thumbnail': self._thumbnail,
            'cover': self._cover,
            'start_timestamp': self._start_timestamp,
            'file_name': self._file_name,
            'mime_type': self._mime_type,
            'file_size': self._file_size,
        }

class VideoNote:
    """This object represents a video message (available in Telegram apps as of v.4.0)."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._length = None
        if 'length' in kwargs:
            self.length = kwargs['length']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._length = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._duration = value

    @property
    def thumbnail(self) -> PhotoSize | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: PhotoSize | None) -> None:
        TypeChecker.check(value, 'PhotoSize | None')
        self._thumbnail = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'length': self._length,
            'duration': self._duration,
            'thumbnail': self._thumbnail,
            'file_size': self._file_size,
        }

class Voice:
    """This object represents a voice note."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._mime_type = None
        if 'mime_type' in kwargs:
            self.mime_type = kwargs['mime_type']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._duration = value

    @property
    def mime_type(self) -> str | None:
        return self._mime_type

    @mime_type.setter
    def mime_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._mime_type = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'duration': self._duration,
            'mime_type': self._mime_type,
            'file_size': self._file_size,
        }

class PaidMediaInfo:
    """Describes the paid media added to a message."""
    def __init__(self, **kwargs: Any):
        self._star_count = None
        if 'star_count' in kwargs:
            self.star_count = kwargs['star_count']
        self._paid_media = None
        if 'paid_media' in kwargs:
            self.paid_media = kwargs['paid_media']

    @property
    def star_count(self) -> int:
        return self._star_count

    @star_count.setter
    def star_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._star_count = value

    @property
    def paid_media(self) -> List[PaidMedia]:
        return self._paid_media

    @paid_media.setter
    def paid_media(self, value: List[PaidMedia]) -> None:
        TypeChecker.check(value, 'List[PaidMedia]')
        self._paid_media = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'star_count': self._star_count,
            'paid_media': self._paid_media,
        }

class PaidMedia:
    """This object describes paid media. Currently, it can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class PaidMediaPreview:
    """The paid media isn't available before the payment."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def width(self) -> int | None:
        return self._width

    @width.setter
    def width(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._width = value

    @property
    def height(self) -> int | None:
        return self._height

    @height.setter
    def height(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._height = value

    @property
    def duration(self) -> int | None:
        return self._duration

    @duration.setter
    def duration(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._duration = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'width': self._width,
            'height': self._height,
            'duration': self._duration,
        }

class PaidMediaPhoto:
    """The paid media is a photo."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._photo = None
        if 'photo' in kwargs:
            self.photo = kwargs['photo']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def photo(self) -> List[PhotoSize]:
        return self._photo

    @photo.setter
    def photo(self, value: List[PhotoSize]) -> None:
        TypeChecker.check(value, 'List[PhotoSize]')
        self._photo = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'photo': self._photo,
        }

class PaidMediaVideo:
    """The paid media is a video."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._video = None
        if 'video' in kwargs:
            self.video = kwargs['video']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def video(self) -> Video:
        return self._video

    @video.setter
    def video(self, value: Video) -> None:
        TypeChecker.check(value, 'Video')
        self._video = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'video': self._video,
        }

class Contact:
    """This object represents a phone contact."""
    def __init__(self, **kwargs: Any):
        self._phone_number = None
        if 'phone_number' in kwargs:
            self.phone_number = kwargs['phone_number']
        self._first_name = None
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        self._last_name = None
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        self._user_id = None
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
        self._vcard = None
        if 'vcard' in kwargs:
            self.vcard = kwargs['vcard']

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._phone_number = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._first_name = value

    @property
    def last_name(self) -> str | None:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._last_name = value

    @property
    def user_id(self) -> int | None:
        return self._user_id

    @user_id.setter
    def user_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._user_id = value

    @property
    def vcard(self) -> str | None:
        return self._vcard

    @vcard.setter
    def vcard(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._vcard = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'phone_number': self._phone_number,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'user_id': self._user_id,
            'vcard': self._vcard,
        }

class Dice:
    """This object represents an animated emoji that displays a random value."""
    def __init__(self, **kwargs: Any):
        self._emoji = None
        if 'emoji' in kwargs:
            self.emoji = kwargs['emoji']
        self._value = None
        if 'value' in kwargs:
            self.value = kwargs['value']

    @property
    def emoji(self) -> str:
        return self._emoji

    @emoji.setter
    def emoji(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._emoji = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._value = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'emoji': self._emoji,
            'value': self._value,
        }

class PollOption:
    """This object contains information about one answer option in a poll."""
    def __init__(self, **kwargs: Any):
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._text_entities = None
        if 'text_entities' in kwargs:
            self.text_entities = kwargs['text_entities']
        self._voter_count = None
        if 'voter_count' in kwargs:
            self.voter_count = kwargs['voter_count']

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._text = value

    @property
    def text_entities(self) -> List[MessageEntity] | None:
        return self._text_entities

    @text_entities.setter
    def text_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._text_entities = value

    @property
    def voter_count(self) -> int:
        return self._voter_count

    @voter_count.setter
    def voter_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._voter_count = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'text': self._text,
            'text_entities': self._text_entities,
            'voter_count': self._voter_count,
        }

class InputPollOption:
    """This object contains information about one answer option in a poll to be sent."""
    def __init__(self, **kwargs: Any):
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._text_parse_mode = None
        if 'text_parse_mode' in kwargs:
            self.text_parse_mode = kwargs['text_parse_mode']
        self._text_entities = None
        if 'text_entities' in kwargs:
            self.text_entities = kwargs['text_entities']

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._text = value

    @property
    def text_parse_mode(self) -> str | None:
        return self._text_parse_mode

    @text_parse_mode.setter
    def text_parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._text_parse_mode = value

    @property
    def text_entities(self) -> List[MessageEntity] | None:
        return self._text_entities

    @text_entities.setter
    def text_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._text_entities = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'text': self._text,
            'text_parse_mode': self._text_parse_mode,
            'text_entities': self._text_entities,
        }

class PollAnswer:
    """This object represents an answer of a user in a non-anonymous poll."""
    def __init__(self, **kwargs: Any):
        self._poll_id = None
        if 'poll_id' in kwargs:
            self.poll_id = kwargs['poll_id']
        self._voter_chat = None
        if 'voter_chat' in kwargs:
            self.voter_chat = kwargs['voter_chat']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._option_ids = None
        if 'option_ids' in kwargs:
            self.option_ids = kwargs['option_ids']

    @property
    def poll_id(self) -> str:
        return self._poll_id

    @poll_id.setter
    def poll_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._poll_id = value

    @property
    def voter_chat(self) -> Chat | None:
        return self._voter_chat

    @voter_chat.setter
    def voter_chat(self, value: Chat | None) -> None:
        TypeChecker.check(value, 'Chat | None')
        self._voter_chat = value

    @property
    def user(self) -> User | None:
        return self._user

    @user.setter
    def user(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._user = value

    @property
    def option_ids(self) -> List[int]:
        return self._option_ids

    @option_ids.setter
    def option_ids(self, value: List[int]) -> None:
        TypeChecker.check(value, 'List[int]')
        self._option_ids = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'poll_id': self._poll_id,
            'voter_chat': self._voter_chat,
            'user': self._user,
            'option_ids': self._option_ids,
        }

class Poll:
    """This object contains information about a poll."""
    def __init__(self, **kwargs: Any):
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']
        self._question = None
        if 'question' in kwargs:
            self.question = kwargs['question']
        self._question_entities = None
        if 'question_entities' in kwargs:
            self.question_entities = kwargs['question_entities']
        self._options = None
        if 'options' in kwargs:
            self.options = kwargs['options']
        self._total_voter_count = None
        if 'total_voter_count' in kwargs:
            self.total_voter_count = kwargs['total_voter_count']
        self._is_closed = None
        if 'is_closed' in kwargs:
            self.is_closed = kwargs['is_closed']
        self._is_anonymous = None
        if 'is_anonymous' in kwargs:
            self.is_anonymous = kwargs['is_anonymous']
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._allows_multiple_answers = None
        if 'allows_multiple_answers' in kwargs:
            self.allows_multiple_answers = kwargs['allows_multiple_answers']
        self._correct_option_id = None
        if 'correct_option_id' in kwargs:
            self.correct_option_id = kwargs['correct_option_id']
        self._explanation = None
        if 'explanation' in kwargs:
            self.explanation = kwargs['explanation']
        self._explanation_entities = None
        if 'explanation_entities' in kwargs:
            self.explanation_entities = kwargs['explanation_entities']
        self._open_period = None
        if 'open_period' in kwargs:
            self.open_period = kwargs['open_period']
        self._close_date = None
        if 'close_date' in kwargs:
            self.close_date = kwargs['close_date']

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._id = value

    @property
    def question(self) -> str:
        return self._question

    @question.setter
    def question(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._question = value

    @property
    def question_entities(self) -> List[MessageEntity] | None:
        return self._question_entities

    @question_entities.setter
    def question_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._question_entities = value

    @property
    def options(self) -> List[PollOption]:
        return self._options

    @options.setter
    def options(self, value: List[PollOption]) -> None:
        TypeChecker.check(value, 'List[PollOption]')
        self._options = value

    @property
    def total_voter_count(self) -> int:
        return self._total_voter_count

    @total_voter_count.setter
    def total_voter_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._total_voter_count = value

    @property
    def is_closed(self) -> bool:
        return self._is_closed

    @is_closed.setter
    def is_closed(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_closed = value

    @property
    def is_anonymous(self) -> bool:
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_anonymous = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def allows_multiple_answers(self) -> bool:
        return self._allows_multiple_answers

    @allows_multiple_answers.setter
    def allows_multiple_answers(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._allows_multiple_answers = value

    @property
    def correct_option_id(self) -> int | None:
        return self._correct_option_id

    @correct_option_id.setter
    def correct_option_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._correct_option_id = value

    @property
    def explanation(self) -> str | None:
        return self._explanation

    @explanation.setter
    def explanation(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._explanation = value

    @property
    def explanation_entities(self) -> List[MessageEntity] | None:
        return self._explanation_entities

    @explanation_entities.setter
    def explanation_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._explanation_entities = value

    @property
    def open_period(self) -> int | None:
        return self._open_period

    @open_period.setter
    def open_period(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._open_period = value

    @property
    def close_date(self) -> int | None:
        return self._close_date

    @close_date.setter
    def close_date(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._close_date = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'question': self._question,
            'question_entities': self._question_entities,
            'options': self._options,
            'total_voter_count': self._total_voter_count,
            'is_closed': self._is_closed,
            'is_anonymous': self._is_anonymous,
            'type': self._type,
            'allows_multiple_answers': self._allows_multiple_answers,
            'correct_option_id': self._correct_option_id,
            'explanation': self._explanation,
            'explanation_entities': self._explanation_entities,
            'open_period': self._open_period,
            'close_date': self._close_date,
        }

class Location:
    """This object represents a point on the map."""
    def __init__(self, **kwargs: Any):
        self._latitude = None
        if 'latitude' in kwargs:
            self.latitude = kwargs['latitude']
        self._longitude = None
        if 'longitude' in kwargs:
            self.longitude = kwargs['longitude']
        self._horizontal_accuracy = None
        if 'horizontal_accuracy' in kwargs:
            self.horizontal_accuracy = kwargs['horizontal_accuracy']
        self._live_period = None
        if 'live_period' in kwargs:
            self.live_period = kwargs['live_period']
        self._heading = None
        if 'heading' in kwargs:
            self.heading = kwargs['heading']
        self._proximity_alert_radius = None
        if 'proximity_alert_radius' in kwargs:
            self.proximity_alert_radius = kwargs['proximity_alert_radius']

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, value: float) -> None:
        TypeChecker.check(value, 'float')
        self._latitude = value

    @property
    def longitude(self) -> float:
        return self._longitude

    @longitude.setter
    def longitude(self, value: float) -> None:
        TypeChecker.check(value, 'float')
        self._longitude = value

    @property
    def horizontal_accuracy(self) -> float | None:
        return self._horizontal_accuracy

    @horizontal_accuracy.setter
    def horizontal_accuracy(self, value: float | None) -> None:
        TypeChecker.check(value, 'float | None')
        self._horizontal_accuracy = value

    @property
    def live_period(self) -> int | None:
        return self._live_period

    @live_period.setter
    def live_period(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._live_period = value

    @property
    def heading(self) -> int | None:
        return self._heading

    @heading.setter
    def heading(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._heading = value

    @property
    def proximity_alert_radius(self) -> int | None:
        return self._proximity_alert_radius

    @proximity_alert_radius.setter
    def proximity_alert_radius(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._proximity_alert_radius = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'latitude': self._latitude,
            'longitude': self._longitude,
            'horizontal_accuracy': self._horizontal_accuracy,
            'live_period': self._live_period,
            'heading': self._heading,
            'proximity_alert_radius': self._proximity_alert_radius,
        }

class Venue:
    """This object represents a venue."""
    def __init__(self, **kwargs: Any):
        self._location = None
        if 'location' in kwargs:
            self.location = kwargs['location']
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']
        self._address = None
        if 'address' in kwargs:
            self.address = kwargs['address']
        self._foursquare_id = None
        if 'foursquare_id' in kwargs:
            self.foursquare_id = kwargs['foursquare_id']
        self._foursquare_type = None
        if 'foursquare_type' in kwargs:
            self.foursquare_type = kwargs['foursquare_type']
        self._google_place_id = None
        if 'google_place_id' in kwargs:
            self.google_place_id = kwargs['google_place_id']
        self._google_place_type = None
        if 'google_place_type' in kwargs:
            self.google_place_type = kwargs['google_place_type']

    @property
    def location(self) -> Location:
        return self._location

    @location.setter
    def location(self, value: Location) -> None:
        TypeChecker.check(value, 'Location')
        self._location = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._title = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._address = value

    @property
    def foursquare_id(self) -> str | None:
        return self._foursquare_id

    @foursquare_id.setter
    def foursquare_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._foursquare_id = value

    @property
    def foursquare_type(self) -> str | None:
        return self._foursquare_type

    @foursquare_type.setter
    def foursquare_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._foursquare_type = value

    @property
    def google_place_id(self) -> str | None:
        return self._google_place_id

    @google_place_id.setter
    def google_place_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._google_place_id = value

    @property
    def google_place_type(self) -> str | None:
        return self._google_place_type

    @google_place_type.setter
    def google_place_type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._google_place_type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'location': self._location,
            'title': self._title,
            'address': self._address,
            'foursquare_id': self._foursquare_id,
            'foursquare_type': self._foursquare_type,
            'google_place_id': self._google_place_id,
            'google_place_type': self._google_place_type,
        }

class WebAppData:
    """Describes data sent from a Web App to the bot."""
    def __init__(self, **kwargs: Any):
        self._data = None
        if 'data' in kwargs:
            self.data = kwargs['data']
        self._button_text = None
        if 'button_text' in kwargs:
            self.button_text = kwargs['button_text']

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._data = value

    @property
    def button_text(self) -> str:
        return self._button_text

    @button_text.setter
    def button_text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._button_text = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'data': self._data,
            'button_text': self._button_text,
        }

class ProximityAlertTriggered:
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user."""
    def __init__(self, **kwargs: Any):
        self._traveler = None
        if 'traveler' in kwargs:
            self.traveler = kwargs['traveler']
        self._watcher = None
        if 'watcher' in kwargs:
            self.watcher = kwargs['watcher']
        self._distance = None
        if 'distance' in kwargs:
            self.distance = kwargs['distance']

    @property
    def traveler(self) -> User:
        return self._traveler

    @traveler.setter
    def traveler(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._traveler = value

    @property
    def watcher(self) -> User:
        return self._watcher

    @watcher.setter
    def watcher(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._watcher = value

    @property
    def distance(self) -> int:
        return self._distance

    @distance.setter
    def distance(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._distance = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'traveler': self._traveler,
            'watcher': self._watcher,
            'distance': self._distance,
        }

class MessageAutoDeleteTimerChanged:
    """This object represents a service message about a change in auto-delete timer settings."""
    def __init__(self, **kwargs: Any):
        self._message_auto_delete_time = None
        if 'message_auto_delete_time' in kwargs:
            self.message_auto_delete_time = kwargs['message_auto_delete_time']

    @property
    def message_auto_delete_time(self) -> int:
        return self._message_auto_delete_time

    @message_auto_delete_time.setter
    def message_auto_delete_time(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_auto_delete_time = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'message_auto_delete_time': self._message_auto_delete_time,
        }

class ChatBoostAdded:
    """This object represents a service message about a user boosting a chat."""
    def __init__(self, **kwargs: Any):
        self._boost_count = None
        if 'boost_count' in kwargs:
            self.boost_count = kwargs['boost_count']

    @property
    def boost_count(self) -> int:
        return self._boost_count

    @boost_count.setter
    def boost_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._boost_count = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'boost_count': self._boost_count,
        }

class BackgroundFill:
    """This object describes the way a background is filled based on the selected colors. Currently, it can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class BackgroundFillSolid:
    """The background is filled using the selected color."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._color = None
        if 'color' in kwargs:
            self.color = kwargs['color']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def color(self) -> int:
        return self._color

    @color.setter
    def color(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._color = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'color': self._color,
        }

class BackgroundFillGradient:
    """The background is a gradient fill."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._top_color = None
        if 'top_color' in kwargs:
            self.top_color = kwargs['top_color']
        self._bottom_color = None
        if 'bottom_color' in kwargs:
            self.bottom_color = kwargs['bottom_color']
        self._rotation_angle = None
        if 'rotation_angle' in kwargs:
            self.rotation_angle = kwargs['rotation_angle']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def top_color(self) -> int:
        return self._top_color

    @top_color.setter
    def top_color(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._top_color = value

    @property
    def bottom_color(self) -> int:
        return self._bottom_color

    @bottom_color.setter
    def bottom_color(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._bottom_color = value

    @property
    def rotation_angle(self) -> int:
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._rotation_angle = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'top_color': self._top_color,
            'bottom_color': self._bottom_color,
            'rotation_angle': self._rotation_angle,
        }

class BackgroundFillFreeformGradient:
    """The background is a freeform gradient that rotates after every message in the chat."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._colors = None
        if 'colors' in kwargs:
            self.colors = kwargs['colors']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def colors(self) -> List[int]:
        return self._colors

    @colors.setter
    def colors(self, value: List[int]) -> None:
        TypeChecker.check(value, 'List[int]')
        self._colors = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'colors': self._colors,
        }

class BackgroundType:
    """This object describes the type of a background. Currently, it can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class BackgroundTypeFill:
    """The background is automatically filled based on the selected colors."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._fill = None
        if 'fill' in kwargs:
            self.fill = kwargs['fill']
        self._dark_theme_dimming = None
        if 'dark_theme_dimming' in kwargs:
            self.dark_theme_dimming = kwargs['dark_theme_dimming']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def fill(self) -> BackgroundFill:
        return self._fill

    @fill.setter
    def fill(self, value: BackgroundFill) -> None:
        TypeChecker.check(value, 'BackgroundFill')
        self._fill = value

    @property
    def dark_theme_dimming(self) -> int:
        return self._dark_theme_dimming

    @dark_theme_dimming.setter
    def dark_theme_dimming(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._dark_theme_dimming = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'fill': self._fill,
            'dark_theme_dimming': self._dark_theme_dimming,
        }

class BackgroundTypeWallpaper:
    """The background is a wallpaper in the JPEG format."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._document = None
        if 'document' in kwargs:
            self.document = kwargs['document']
        self._dark_theme_dimming = None
        if 'dark_theme_dimming' in kwargs:
            self.dark_theme_dimming = kwargs['dark_theme_dimming']
        self._is_blurred = None
        if 'is_blurred' in kwargs:
            self.is_blurred = kwargs['is_blurred']
        self._is_moving = None
        if 'is_moving' in kwargs:
            self.is_moving = kwargs['is_moving']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, value: Document) -> None:
        TypeChecker.check(value, 'Document')
        self._document = value

    @property
    def dark_theme_dimming(self) -> int:
        return self._dark_theme_dimming

    @dark_theme_dimming.setter
    def dark_theme_dimming(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._dark_theme_dimming = value

    @property
    def is_blurred(self) -> bool | None:
        return self._is_blurred

    @is_blurred.setter
    def is_blurred(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_blurred = value

    @property
    def is_moving(self) -> bool | None:
        return self._is_moving

    @is_moving.setter
    def is_moving(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_moving = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'document': self._document,
            'dark_theme_dimming': self._dark_theme_dimming,
            'is_blurred': self._is_blurred,
            'is_moving': self._is_moving,
        }

class BackgroundTypePattern:
    """The background is a .PNG or .TGV (gzipped subset of SVG with MIME type “application/x-tgwallpattern”) pattern to be combined with the background fill chosen by the user."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._document = None
        if 'document' in kwargs:
            self.document = kwargs['document']
        self._fill = None
        if 'fill' in kwargs:
            self.fill = kwargs['fill']
        self._intensity = None
        if 'intensity' in kwargs:
            self.intensity = kwargs['intensity']
        self._is_inverted = None
        if 'is_inverted' in kwargs:
            self.is_inverted = kwargs['is_inverted']
        self._is_moving = None
        if 'is_moving' in kwargs:
            self.is_moving = kwargs['is_moving']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, value: Document) -> None:
        TypeChecker.check(value, 'Document')
        self._document = value

    @property
    def fill(self) -> BackgroundFill:
        return self._fill

    @fill.setter
    def fill(self, value: BackgroundFill) -> None:
        TypeChecker.check(value, 'BackgroundFill')
        self._fill = value

    @property
    def intensity(self) -> int:
        return self._intensity

    @intensity.setter
    def intensity(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._intensity = value

    @property
    def is_inverted(self) -> bool | None:
        return self._is_inverted

    @is_inverted.setter
    def is_inverted(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_inverted = value

    @property
    def is_moving(self) -> bool | None:
        return self._is_moving

    @is_moving.setter
    def is_moving(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_moving = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'document': self._document,
            'fill': self._fill,
            'intensity': self._intensity,
            'is_inverted': self._is_inverted,
            'is_moving': self._is_moving,
        }

class BackgroundTypeChatTheme:
    """The background is taken directly from a built-in chat theme."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._theme_name = None
        if 'theme_name' in kwargs:
            self.theme_name = kwargs['theme_name']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def theme_name(self) -> str:
        return self._theme_name

    @theme_name.setter
    def theme_name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._theme_name = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'theme_name': self._theme_name,
        }

class ChatBackground:
    """This object represents a chat background."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> BackgroundType:
        return self._type

    @type.setter
    def type(self, value: BackgroundType) -> None:
        TypeChecker.check(value, 'BackgroundType')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class ForumTopicCreated:
    """This object represents a service message about a new forum topic created in the chat."""
    def __init__(self, **kwargs: Any):
        self._name = None
        if 'name' in kwargs:
            self.name = kwargs['name']
        self._icon_color = None
        if 'icon_color' in kwargs:
            self.icon_color = kwargs['icon_color']
        self._icon_custom_emoji_id = None
        if 'icon_custom_emoji_id' in kwargs:
            self.icon_custom_emoji_id = kwargs['icon_custom_emoji_id']

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._name = value

    @property
    def icon_color(self) -> int:
        return self._icon_color

    @icon_color.setter
    def icon_color(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._icon_color = value

    @property
    def icon_custom_emoji_id(self) -> str | None:
        return self._icon_custom_emoji_id

    @icon_custom_emoji_id.setter
    def icon_custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._icon_custom_emoji_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self._name,
            'icon_color': self._icon_color,
            'icon_custom_emoji_id': self._icon_custom_emoji_id,
        }

class ForumTopicClosed:
    """This object represents a service message about a forum topic closed in the chat. Currently holds no information."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class ForumTopicEdited:
    """This object represents a service message about an edited forum topic."""
    def __init__(self, **kwargs: Any):
        self._name = None
        if 'name' in kwargs:
            self.name = kwargs['name']
        self._icon_custom_emoji_id = None
        if 'icon_custom_emoji_id' in kwargs:
            self.icon_custom_emoji_id = kwargs['icon_custom_emoji_id']

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._name = value

    @property
    def icon_custom_emoji_id(self) -> str | None:
        return self._icon_custom_emoji_id

    @icon_custom_emoji_id.setter
    def icon_custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._icon_custom_emoji_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self._name,
            'icon_custom_emoji_id': self._icon_custom_emoji_id,
        }

class ForumTopicReopened:
    """This object represents a service message about a forum topic reopened in the chat. Currently holds no information."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class GeneralForumTopicHidden:
    """This object represents a service message about General forum topic hidden in the chat. Currently holds no information."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class GeneralForumTopicUnhidden:
    """This object represents a service message about General forum topic unhidden in the chat. Currently holds no information."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class SharedUser:
    """This object contains information about a user that was shared with the bot using a KeyboardButtonRequestUsers button."""
    def __init__(self, **kwargs: Any):
        self._user_id = None
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
        self._first_name = None
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        self._last_name = None
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        self._username = None
        if 'username' in kwargs:
            self.username = kwargs['username']
        self._photo = None
        if 'photo' in kwargs:
            self.photo = kwargs['photo']

    @property
    def user_id(self) -> int:
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._user_id = value

    @property
    def first_name(self) -> str | None:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._first_name = value

    @property
    def last_name(self) -> str | None:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._last_name = value

    @property
    def username(self) -> str | None:
        return self._username

    @username.setter
    def username(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._username = value

    @property
    def photo(self) -> List[PhotoSize] | None:
        return self._photo

    @photo.setter
    def photo(self, value: List[PhotoSize] | None) -> None:
        TypeChecker.check(value, 'List[PhotoSize] | None')
        self._photo = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'user_id': self._user_id,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'username': self._username,
            'photo': self._photo,
        }

class UsersShared:
    """This object contains information about the users whose identifiers were shared with the bot using a KeyboardButtonRequestUsers button."""
    def __init__(self, **kwargs: Any):
        self._request_id = None
        if 'request_id' in kwargs:
            self.request_id = kwargs['request_id']
        self._users = None
        if 'users' in kwargs:
            self.users = kwargs['users']

    @property
    def request_id(self) -> int:
        return self._request_id

    @request_id.setter
    def request_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._request_id = value

    @property
    def users(self) -> List[SharedUser]:
        return self._users

    @users.setter
    def users(self, value: List[SharedUser]) -> None:
        TypeChecker.check(value, 'List[SharedUser]')
        self._users = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'request_id': self._request_id,
            'users': self._users,
        }

class ChatShared:
    """This object contains information about a chat that was shared with the bot using a KeyboardButtonRequestChat button."""
    def __init__(self, **kwargs: Any):
        self._request_id = None
        if 'request_id' in kwargs:
            self.request_id = kwargs['request_id']
        self._chat_id = None
        if 'chat_id' in kwargs:
            self.chat_id = kwargs['chat_id']
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']
        self._username = None
        if 'username' in kwargs:
            self.username = kwargs['username']
        self._photo = None
        if 'photo' in kwargs:
            self.photo = kwargs['photo']

    @property
    def request_id(self) -> int:
        return self._request_id

    @request_id.setter
    def request_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._request_id = value

    @property
    def chat_id(self) -> int:
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._chat_id = value

    @property
    def title(self) -> str | None:
        return self._title

    @title.setter
    def title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._title = value

    @property
    def username(self) -> str | None:
        return self._username

    @username.setter
    def username(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._username = value

    @property
    def photo(self) -> List[PhotoSize] | None:
        return self._photo

    @photo.setter
    def photo(self, value: List[PhotoSize] | None) -> None:
        TypeChecker.check(value, 'List[PhotoSize] | None')
        self._photo = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'request_id': self._request_id,
            'chat_id': self._chat_id,
            'title': self._title,
            'username': self._username,
            'photo': self._photo,
        }

class WriteAccessAllowed:
    """This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess."""
    def __init__(self, **kwargs: Any):
        self._from_request = None
        if 'from_request' in kwargs:
            self.from_request = kwargs['from_request']
        self._web_app_name = None
        if 'web_app_name' in kwargs:
            self.web_app_name = kwargs['web_app_name']
        self._from_attachment_menu = None
        if 'from_attachment_menu' in kwargs:
            self.from_attachment_menu = kwargs['from_attachment_menu']

    @property
    def from_request(self) -> bool | None:
        return self._from_request

    @from_request.setter
    def from_request(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._from_request = value

    @property
    def web_app_name(self) -> str | None:
        return self._web_app_name

    @web_app_name.setter
    def web_app_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._web_app_name = value

    @property
    def from_attachment_menu(self) -> bool | None:
        return self._from_attachment_menu

    @from_attachment_menu.setter
    def from_attachment_menu(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._from_attachment_menu = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'from_request': self._from_request,
            'web_app_name': self._web_app_name,
            'from_attachment_menu': self._from_attachment_menu,
        }

class VideoChatScheduled:
    """This object represents a service message about a video chat scheduled in the chat."""
    def __init__(self, **kwargs: Any):
        self._start_date = None
        if 'start_date' in kwargs:
            self.start_date = kwargs['start_date']

    @property
    def start_date(self) -> int:
        return self._start_date

    @start_date.setter
    def start_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._start_date = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'start_date': self._start_date,
        }

class VideoChatStarted:
    """This object represents a service message about a video chat started in the chat. Currently holds no information."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class VideoChatEnded:
    """This object represents a service message about a video chat ended in the chat."""
    def __init__(self, **kwargs: Any):
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._duration = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'duration': self._duration,
        }

class VideoChatParticipantsInvited:
    """This object represents a service message about new members invited to a video chat."""
    def __init__(self, **kwargs: Any):
        self._users = None
        if 'users' in kwargs:
            self.users = kwargs['users']

    @property
    def users(self) -> List[User]:
        return self._users

    @users.setter
    def users(self, value: List[User]) -> None:
        TypeChecker.check(value, 'List[User]')
        self._users = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'users': self._users,
        }

class GiveawayCreated:
    """This object represents a service message about the creation of a scheduled giveaway."""
    def __init__(self, **kwargs: Any):
        self._prize_star_count = None
        if 'prize_star_count' in kwargs:
            self.prize_star_count = kwargs['prize_star_count']

    @property
    def prize_star_count(self) -> int | None:
        return self._prize_star_count

    @prize_star_count.setter
    def prize_star_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._prize_star_count = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'prize_star_count': self._prize_star_count,
        }

class Giveaway:
    """This object represents a message about a scheduled giveaway."""
    def __init__(self, **kwargs: Any):
        self._chats = None
        if 'chats' in kwargs:
            self.chats = kwargs['chats']
        self._winners_selection_date = None
        if 'winners_selection_date' in kwargs:
            self.winners_selection_date = kwargs['winners_selection_date']
        self._winner_count = None
        if 'winner_count' in kwargs:
            self.winner_count = kwargs['winner_count']
        self._only_new_members = None
        if 'only_new_members' in kwargs:
            self.only_new_members = kwargs['only_new_members']
        self._has_public_winners = None
        if 'has_public_winners' in kwargs:
            self.has_public_winners = kwargs['has_public_winners']
        self._prize_description = None
        if 'prize_description' in kwargs:
            self.prize_description = kwargs['prize_description']
        self._country_codes = None
        if 'country_codes' in kwargs:
            self.country_codes = kwargs['country_codes']
        self._prize_star_count = None
        if 'prize_star_count' in kwargs:
            self.prize_star_count = kwargs['prize_star_count']
        self._premium_subscription_month_count = None
        if 'premium_subscription_month_count' in kwargs:
            self.premium_subscription_month_count = kwargs['premium_subscription_month_count']

    @property
    def chats(self) -> List[Chat]:
        return self._chats

    @chats.setter
    def chats(self, value: List[Chat]) -> None:
        TypeChecker.check(value, 'List[Chat]')
        self._chats = value

    @property
    def winners_selection_date(self) -> int:
        return self._winners_selection_date

    @winners_selection_date.setter
    def winners_selection_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._winners_selection_date = value

    @property
    def winner_count(self) -> int:
        return self._winner_count

    @winner_count.setter
    def winner_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._winner_count = value

    @property
    def only_new_members(self) -> bool | None:
        return self._only_new_members

    @only_new_members.setter
    def only_new_members(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._only_new_members = value

    @property
    def has_public_winners(self) -> bool | None:
        return self._has_public_winners

    @has_public_winners.setter
    def has_public_winners(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_public_winners = value

    @property
    def prize_description(self) -> str | None:
        return self._prize_description

    @prize_description.setter
    def prize_description(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._prize_description = value

    @property
    def country_codes(self) -> List[str] | None:
        return self._country_codes

    @country_codes.setter
    def country_codes(self, value: List[str] | None) -> None:
        TypeChecker.check(value, 'List[str] | None')
        self._country_codes = value

    @property
    def prize_star_count(self) -> int | None:
        return self._prize_star_count

    @prize_star_count.setter
    def prize_star_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._prize_star_count = value

    @property
    def premium_subscription_month_count(self) -> int | None:
        return self._premium_subscription_month_count

    @premium_subscription_month_count.setter
    def premium_subscription_month_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._premium_subscription_month_count = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chats': self._chats,
            'winners_selection_date': self._winners_selection_date,
            'winner_count': self._winner_count,
            'only_new_members': self._only_new_members,
            'has_public_winners': self._has_public_winners,
            'prize_description': self._prize_description,
            'country_codes': self._country_codes,
            'prize_star_count': self._prize_star_count,
            'premium_subscription_month_count': self._premium_subscription_month_count,
        }

class GiveawayWinners:
    """This object represents a message about the completion of a giveaway with public winners."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._giveaway_message_id = None
        if 'giveaway_message_id' in kwargs:
            self.giveaway_message_id = kwargs['giveaway_message_id']
        self._winners_selection_date = None
        if 'winners_selection_date' in kwargs:
            self.winners_selection_date = kwargs['winners_selection_date']
        self._winner_count = None
        if 'winner_count' in kwargs:
            self.winner_count = kwargs['winner_count']
        self._winners = None
        if 'winners' in kwargs:
            self.winners = kwargs['winners']
        self._additional_chat_count = None
        if 'additional_chat_count' in kwargs:
            self.additional_chat_count = kwargs['additional_chat_count']
        self._prize_star_count = None
        if 'prize_star_count' in kwargs:
            self.prize_star_count = kwargs['prize_star_count']
        self._premium_subscription_month_count = None
        if 'premium_subscription_month_count' in kwargs:
            self.premium_subscription_month_count = kwargs['premium_subscription_month_count']
        self._unclaimed_prize_count = None
        if 'unclaimed_prize_count' in kwargs:
            self.unclaimed_prize_count = kwargs['unclaimed_prize_count']
        self._only_new_members = None
        if 'only_new_members' in kwargs:
            self.only_new_members = kwargs['only_new_members']
        self._was_refunded = None
        if 'was_refunded' in kwargs:
            self.was_refunded = kwargs['was_refunded']
        self._prize_description = None
        if 'prize_description' in kwargs:
            self.prize_description = kwargs['prize_description']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def giveaway_message_id(self) -> int:
        return self._giveaway_message_id

    @giveaway_message_id.setter
    def giveaway_message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._giveaway_message_id = value

    @property
    def winners_selection_date(self) -> int:
        return self._winners_selection_date

    @winners_selection_date.setter
    def winners_selection_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._winners_selection_date = value

    @property
    def winner_count(self) -> int:
        return self._winner_count

    @winner_count.setter
    def winner_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._winner_count = value

    @property
    def winners(self) -> List[User]:
        return self._winners

    @winners.setter
    def winners(self, value: List[User]) -> None:
        TypeChecker.check(value, 'List[User]')
        self._winners = value

    @property
    def additional_chat_count(self) -> int | None:
        return self._additional_chat_count

    @additional_chat_count.setter
    def additional_chat_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._additional_chat_count = value

    @property
    def prize_star_count(self) -> int | None:
        return self._prize_star_count

    @prize_star_count.setter
    def prize_star_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._prize_star_count = value

    @property
    def premium_subscription_month_count(self) -> int | None:
        return self._premium_subscription_month_count

    @premium_subscription_month_count.setter
    def premium_subscription_month_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._premium_subscription_month_count = value

    @property
    def unclaimed_prize_count(self) -> int | None:
        return self._unclaimed_prize_count

    @unclaimed_prize_count.setter
    def unclaimed_prize_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._unclaimed_prize_count = value

    @property
    def only_new_members(self) -> bool | None:
        return self._only_new_members

    @only_new_members.setter
    def only_new_members(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._only_new_members = value

    @property
    def was_refunded(self) -> bool | None:
        return self._was_refunded

    @was_refunded.setter
    def was_refunded(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._was_refunded = value

    @property
    def prize_description(self) -> str | None:
        return self._prize_description

    @prize_description.setter
    def prize_description(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._prize_description = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'giveaway_message_id': self._giveaway_message_id,
            'winners_selection_date': self._winners_selection_date,
            'winner_count': self._winner_count,
            'winners': self._winners,
            'additional_chat_count': self._additional_chat_count,
            'prize_star_count': self._prize_star_count,
            'premium_subscription_month_count': self._premium_subscription_month_count,
            'unclaimed_prize_count': self._unclaimed_prize_count,
            'only_new_members': self._only_new_members,
            'was_refunded': self._was_refunded,
            'prize_description': self._prize_description,
        }

class GiveawayCompleted:
    """This object represents a service message about the completion of a giveaway without public winners."""
    def __init__(self, **kwargs: Any):
        self._winner_count = None
        if 'winner_count' in kwargs:
            self.winner_count = kwargs['winner_count']
        self._unclaimed_prize_count = None
        if 'unclaimed_prize_count' in kwargs:
            self.unclaimed_prize_count = kwargs['unclaimed_prize_count']
        self._giveaway_message = None
        if 'giveaway_message' in kwargs:
            self.giveaway_message = kwargs['giveaway_message']
        self._is_star_giveaway = None
        if 'is_star_giveaway' in kwargs:
            self.is_star_giveaway = kwargs['is_star_giveaway']

    @property
    def winner_count(self) -> int:
        return self._winner_count

    @winner_count.setter
    def winner_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._winner_count = value

    @property
    def unclaimed_prize_count(self) -> int | None:
        return self._unclaimed_prize_count

    @unclaimed_prize_count.setter
    def unclaimed_prize_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._unclaimed_prize_count = value

    @property
    def giveaway_message(self) -> Message | None:
        return self._giveaway_message

    @giveaway_message.setter
    def giveaway_message(self, value: Message | None) -> None:
        TypeChecker.check(value, 'Message | None')
        self._giveaway_message = value

    @property
    def is_star_giveaway(self) -> bool | None:
        return self._is_star_giveaway

    @is_star_giveaway.setter
    def is_star_giveaway(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_star_giveaway = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'winner_count': self._winner_count,
            'unclaimed_prize_count': self._unclaimed_prize_count,
            'giveaway_message': self._giveaway_message,
            'is_star_giveaway': self._is_star_giveaway,
        }

class LinkPreviewOptions:
    """Describes the options used for link preview generation."""
    def __init__(self, **kwargs: Any):
        self._is_disabled = None
        if 'is_disabled' in kwargs:
            self.is_disabled = kwargs['is_disabled']
        self._url = None
        if 'url' in kwargs:
            self.url = kwargs['url']
        self._prefer_small_media = None
        if 'prefer_small_media' in kwargs:
            self.prefer_small_media = kwargs['prefer_small_media']
        self._prefer_large_media = None
        if 'prefer_large_media' in kwargs:
            self.prefer_large_media = kwargs['prefer_large_media']
        self._show_above_text = None
        if 'show_above_text' in kwargs:
            self.show_above_text = kwargs['show_above_text']

    @property
    def is_disabled(self) -> bool | None:
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_disabled = value

    @property
    def url(self) -> str | None:
        return self._url

    @url.setter
    def url(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._url = value

    @property
    def prefer_small_media(self) -> bool | None:
        return self._prefer_small_media

    @prefer_small_media.setter
    def prefer_small_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._prefer_small_media = value

    @property
    def prefer_large_media(self) -> bool | None:
        return self._prefer_large_media

    @prefer_large_media.setter
    def prefer_large_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._prefer_large_media = value

    @property
    def show_above_text(self) -> bool | None:
        return self._show_above_text

    @show_above_text.setter
    def show_above_text(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._show_above_text = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'is_disabled': self._is_disabled,
            'url': self._url,
            'prefer_small_media': self._prefer_small_media,
            'prefer_large_media': self._prefer_large_media,
            'show_above_text': self._show_above_text,
        }

class UserProfilePhotos:
    """This object represent a user's profile pictures."""
    def __init__(self, **kwargs: Any):
        self._total_count = None
        if 'total_count' in kwargs:
            self.total_count = kwargs['total_count']
        self._photos = None
        if 'photos' in kwargs:
            self.photos = kwargs['photos']

    @property
    def total_count(self) -> int:
        return self._total_count

    @total_count.setter
    def total_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._total_count = value

    @property
    def photos(self) -> List[PhotoSize]:
        return self._photos

    @photos.setter
    def photos(self, value: List[PhotoSize]) -> None:
        TypeChecker.check(value, 'List[PhotoSize]')
        self._photos = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'total_count': self._total_count,
            'photos': self._photos,
        }

class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile."""
    def __init__(self, **kwargs: Any):
        self._file_id = None
        if 'file_id' in kwargs:
            self.file_id = kwargs['file_id']
        self._file_unique_id = None
        if 'file_unique_id' in kwargs:
            self.file_unique_id = kwargs['file_unique_id']
        self._file_size = None
        if 'file_size' in kwargs:
            self.file_size = kwargs['file_size']
        self._file_path = None
        if 'file_path' in kwargs:
            self.file_path = kwargs['file_path']

    @property
    def file_id(self) -> str:
        return self._file_id

    @file_id.setter
    def file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_id = value

    @property
    def file_unique_id(self) -> str:
        return self._file_unique_id

    @file_unique_id.setter
    def file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._file_unique_id = value

    @property
    def file_size(self) -> int | None:
        return self._file_size

    @file_size.setter
    def file_size(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._file_size = value

    @property
    def file_path(self) -> str | None:
        return self._file_path

    @file_path.setter
    def file_path(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._file_path = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'file_id': self._file_id,
            'file_unique_id': self._file_unique_id,
            'file_size': self._file_size,
            'file_path': self._file_path,
        }

class WebAppInfo:
    """Describes a Web App."""
    def __init__(self, **kwargs: Any):
        self._url = None
        if 'url' in kwargs:
            self.url = kwargs['url']

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._url = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'url': self._url,
        }

class ReplyKeyboardMarkup:
    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples). Not supported in channels and for messages sent on behalf of a Telegram Business account."""
    def __init__(self, **kwargs: Any):
        self._keyboard = None
        if 'keyboard' in kwargs:
            self.keyboard = kwargs['keyboard']
        self._is_persistent = None
        if 'is_persistent' in kwargs:
            self.is_persistent = kwargs['is_persistent']
        self._resize_keyboard = None
        if 'resize_keyboard' in kwargs:
            self.resize_keyboard = kwargs['resize_keyboard']
        self._one_time_keyboard = None
        if 'one_time_keyboard' in kwargs:
            self.one_time_keyboard = kwargs['one_time_keyboard']
        self._input_field_placeholder = None
        if 'input_field_placeholder' in kwargs:
            self.input_field_placeholder = kwargs['input_field_placeholder']
        self._selective = None
        if 'selective' in kwargs:
            self.selective = kwargs['selective']

    @property
    def keyboard(self) -> List[KeyboardButton]:
        return self._keyboard

    @keyboard.setter
    def keyboard(self, value: List[KeyboardButton]) -> None:
        TypeChecker.check(value, 'List[KeyboardButton]')
        self._keyboard = value

    @property
    def is_persistent(self) -> bool | None:
        return self._is_persistent

    @is_persistent.setter
    def is_persistent(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_persistent = value

    @property
    def resize_keyboard(self) -> bool | None:
        return self._resize_keyboard

    @resize_keyboard.setter
    def resize_keyboard(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._resize_keyboard = value

    @property
    def one_time_keyboard(self) -> bool | None:
        return self._one_time_keyboard

    @one_time_keyboard.setter
    def one_time_keyboard(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._one_time_keyboard = value

    @property
    def input_field_placeholder(self) -> str | None:
        return self._input_field_placeholder

    @input_field_placeholder.setter
    def input_field_placeholder(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._input_field_placeholder = value

    @property
    def selective(self) -> bool | None:
        return self._selective

    @selective.setter
    def selective(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._selective = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'keyboard': self._keyboard,
            'is_persistent': self._is_persistent,
            'resize_keyboard': self._resize_keyboard,
            'one_time_keyboard': self._one_time_keyboard,
            'input_field_placeholder': self._input_field_placeholder,
            'selective': self._selective,
        }

class KeyboardButton:
    """This object represents one button of the reply keyboard. At most one of the optional fields must be used to specify type of the button. For simple text buttons, String can be used instead of this object to specify the button text."""
    def __init__(self, **kwargs: Any):
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._request_users = None
        if 'request_users' in kwargs:
            self.request_users = kwargs['request_users']
        self._request_chat = None
        if 'request_chat' in kwargs:
            self.request_chat = kwargs['request_chat']
        self._request_contact = None
        if 'request_contact' in kwargs:
            self.request_contact = kwargs['request_contact']
        self._request_location = None
        if 'request_location' in kwargs:
            self.request_location = kwargs['request_location']
        self._request_poll = None
        if 'request_poll' in kwargs:
            self.request_poll = kwargs['request_poll']
        self._web_app = None
        if 'web_app' in kwargs:
            self.web_app = kwargs['web_app']

    @property
    def text(self) -> str | None:
        return self._text

    @text.setter
    def text(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._text = value

    @property
    def request_users(self) -> KeyboardButtonRequestUsers | None:
        return self._request_users

    @request_users.setter
    def request_users(self, value: KeyboardButtonRequestUsers | None) -> None:
        TypeChecker.check(value, 'KeyboardButtonRequestUsers | None')
        self._request_users = value

    @property
    def request_chat(self) -> KeyboardButtonRequestChat | None:
        return self._request_chat

    @request_chat.setter
    def request_chat(self, value: KeyboardButtonRequestChat | None) -> None:
        TypeChecker.check(value, 'KeyboardButtonRequestChat | None')
        self._request_chat = value

    @property
    def request_contact(self) -> bool | None:
        return self._request_contact

    @request_contact.setter
    def request_contact(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_contact = value

    @property
    def request_location(self) -> bool | None:
        return self._request_location

    @request_location.setter
    def request_location(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_location = value

    @property
    def request_poll(self) -> KeyboardButtonPollType | None:
        return self._request_poll

    @request_poll.setter
    def request_poll(self, value: KeyboardButtonPollType | None) -> None:
        TypeChecker.check(value, 'KeyboardButtonPollType | None')
        self._request_poll = value

    @property
    def web_app(self) -> WebAppInfo | None:
        return self._web_app

    @web_app.setter
    def web_app(self, value: WebAppInfo | None) -> None:
        TypeChecker.check(value, 'WebAppInfo | None')
        self._web_app = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'text': self._text,
            'request_users': self._request_users,
            'request_chat': self._request_chat,
            'request_contact': self._request_contact,
            'request_location': self._request_location,
            'request_poll': self._request_poll,
            'web_app': self._web_app,
        }

class KeyboardButtonRequestUsers:
    """This object defines the criteria used to request suitable users. Information about the selected users will be shared with the bot when the corresponding button is pressed. More about requesting users »"""
    def __init__(self, **kwargs: Any):
        self._request_id = None
        if 'request_id' in kwargs:
            self.request_id = kwargs['request_id']
        self._user_is_bot = None
        if 'user_is_bot' in kwargs:
            self.user_is_bot = kwargs['user_is_bot']
        self._user_is_premium = None
        if 'user_is_premium' in kwargs:
            self.user_is_premium = kwargs['user_is_premium']
        self._max_quantity = None
        if 'max_quantity' in kwargs:
            self.max_quantity = kwargs['max_quantity']
        self._request_name = None
        if 'request_name' in kwargs:
            self.request_name = kwargs['request_name']
        self._request_username = None
        if 'request_username' in kwargs:
            self.request_username = kwargs['request_username']
        self._request_photo = None
        if 'request_photo' in kwargs:
            self.request_photo = kwargs['request_photo']

    @property
    def request_id(self) -> int:
        return self._request_id

    @request_id.setter
    def request_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._request_id = value

    @property
    def user_is_bot(self) -> bool | None:
        return self._user_is_bot

    @user_is_bot.setter
    def user_is_bot(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._user_is_bot = value

    @property
    def user_is_premium(self) -> bool | None:
        return self._user_is_premium

    @user_is_premium.setter
    def user_is_premium(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._user_is_premium = value

    @property
    def max_quantity(self) -> int | None:
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._max_quantity = value

    @property
    def request_name(self) -> bool | None:
        return self._request_name

    @request_name.setter
    def request_name(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_name = value

    @property
    def request_username(self) -> bool | None:
        return self._request_username

    @request_username.setter
    def request_username(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_username = value

    @property
    def request_photo(self) -> bool | None:
        return self._request_photo

    @request_photo.setter
    def request_photo(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_photo = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'request_id': self._request_id,
            'user_is_bot': self._user_is_bot,
            'user_is_premium': self._user_is_premium,
            'max_quantity': self._max_quantity,
            'request_name': self._request_name,
            'request_username': self._request_username,
            'request_photo': self._request_photo,
        }

class KeyboardButtonRequestChat:
    """This object defines the criteria used to request a suitable chat. Information about the selected chat will be shared with the bot when the corresponding button is pressed. The bot will be granted requested rights in the chat if appropriate. More about requesting chats »."""
    def __init__(self, **kwargs: Any):
        self._request_id = None
        if 'request_id' in kwargs:
            self.request_id = kwargs['request_id']
        self._chat_is_channel = None
        if 'chat_is_channel' in kwargs:
            self.chat_is_channel = kwargs['chat_is_channel']
        self._chat_is_forum = None
        if 'chat_is_forum' in kwargs:
            self.chat_is_forum = kwargs['chat_is_forum']
        self._chat_has_username = None
        if 'chat_has_username' in kwargs:
            self.chat_has_username = kwargs['chat_has_username']
        self._chat_is_created = None
        if 'chat_is_created' in kwargs:
            self.chat_is_created = kwargs['chat_is_created']
        self._user_administrator_rights = None
        if 'user_administrator_rights' in kwargs:
            self.user_administrator_rights = kwargs['user_administrator_rights']
        self._bot_administrator_rights = None
        if 'bot_administrator_rights' in kwargs:
            self.bot_administrator_rights = kwargs['bot_administrator_rights']
        self._bot_is_member = None
        if 'bot_is_member' in kwargs:
            self.bot_is_member = kwargs['bot_is_member']
        self._request_title = None
        if 'request_title' in kwargs:
            self.request_title = kwargs['request_title']
        self._request_username = None
        if 'request_username' in kwargs:
            self.request_username = kwargs['request_username']
        self._request_photo = None
        if 'request_photo' in kwargs:
            self.request_photo = kwargs['request_photo']

    @property
    def request_id(self) -> int:
        return self._request_id

    @request_id.setter
    def request_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._request_id = value

    @property
    def chat_is_channel(self) -> bool:
        return self._chat_is_channel

    @chat_is_channel.setter
    def chat_is_channel(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._chat_is_channel = value

    @property
    def chat_is_forum(self) -> bool | None:
        return self._chat_is_forum

    @chat_is_forum.setter
    def chat_is_forum(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._chat_is_forum = value

    @property
    def chat_has_username(self) -> bool | None:
        return self._chat_has_username

    @chat_has_username.setter
    def chat_has_username(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._chat_has_username = value

    @property
    def chat_is_created(self) -> bool | None:
        return self._chat_is_created

    @chat_is_created.setter
    def chat_is_created(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._chat_is_created = value

    @property
    def user_administrator_rights(self) -> ChatAdministratorRights | None:
        return self._user_administrator_rights

    @user_administrator_rights.setter
    def user_administrator_rights(self, value: ChatAdministratorRights | None) -> None:
        TypeChecker.check(value, 'ChatAdministratorRights | None')
        self._user_administrator_rights = value

    @property
    def bot_administrator_rights(self) -> ChatAdministratorRights | None:
        return self._bot_administrator_rights

    @bot_administrator_rights.setter
    def bot_administrator_rights(self, value: ChatAdministratorRights | None) -> None:
        TypeChecker.check(value, 'ChatAdministratorRights | None')
        self._bot_administrator_rights = value

    @property
    def bot_is_member(self) -> bool | None:
        return self._bot_is_member

    @bot_is_member.setter
    def bot_is_member(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._bot_is_member = value

    @property
    def request_title(self) -> bool | None:
        return self._request_title

    @request_title.setter
    def request_title(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_title = value

    @property
    def request_username(self) -> bool | None:
        return self._request_username

    @request_username.setter
    def request_username(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_username = value

    @property
    def request_photo(self) -> bool | None:
        return self._request_photo

    @request_photo.setter
    def request_photo(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_photo = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'request_id': self._request_id,
            'chat_is_channel': self._chat_is_channel,
            'chat_is_forum': self._chat_is_forum,
            'chat_has_username': self._chat_has_username,
            'chat_is_created': self._chat_is_created,
            'user_administrator_rights': self._user_administrator_rights,
            'bot_administrator_rights': self._bot_administrator_rights,
            'bot_is_member': self._bot_is_member,
            'request_title': self._request_title,
            'request_username': self._request_username,
            'request_photo': self._request_photo,
        }

class KeyboardButtonPollType:
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str | None:
        return self._type

    @type.setter
    def type(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class ReplyKeyboardRemove:
    """Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup). Not supported in channels and for messages sent on behalf of a Telegram Business account."""
    def __init__(self, **kwargs: Any):
        self._remove_keyboard = None
        if 'remove_keyboard' in kwargs:
            self.remove_keyboard = kwargs['remove_keyboard']
        self._selective = None
        if 'selective' in kwargs:
            self.selective = kwargs['selective']

    @property
    def remove_keyboard(self) -> bool:
        return self._remove_keyboard

    @remove_keyboard.setter
    def remove_keyboard(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._remove_keyboard = value

    @property
    def selective(self) -> bool | None:
        return self._selective

    @selective.setter
    def selective(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._selective = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'remove_keyboard': self._remove_keyboard,
            'selective': self._selective,
        }

class InlineKeyboardMarkup:
    """This object represents an inline keyboard that appears right next to the message it belongs to."""
    def __init__(self, **kwargs: Any):
        self._inline_keyboard = None
        if 'inline_keyboard' in kwargs:
            self.inline_keyboard = kwargs['inline_keyboard']

    @property
    def inline_keyboard(self) -> List[InlineKeyboardButton]:
        return self._inline_keyboard

    @inline_keyboard.setter
    def inline_keyboard(self, value: List[InlineKeyboardButton]) -> None:
        TypeChecker.check(value, 'List[InlineKeyboardButton]')
        self._inline_keyboard = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'inline_keyboard': self._inline_keyboard,
        }

class InlineKeyboardButton:
    """This object represents one button of an inline keyboard. Exactly one of the optional fields must be used to specify type of the button."""
    def __init__(self, **kwargs: Any):
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._url = None
        if 'url' in kwargs:
            self.url = kwargs['url']
        self._callback_data = None
        if 'callback_data' in kwargs:
            self.callback_data = kwargs['callback_data']
        self._web_app = None
        if 'web_app' in kwargs:
            self.web_app = kwargs['web_app']
        self._login_url = None
        if 'login_url' in kwargs:
            self.login_url = kwargs['login_url']
        self._switch_inline_query = None
        if 'switch_inline_query' in kwargs:
            self.switch_inline_query = kwargs['switch_inline_query']
        self._switch_inline_query_current_chat = None
        if 'switch_inline_query_current_chat' in kwargs:
            self.switch_inline_query_current_chat = kwargs['switch_inline_query_current_chat']
        self._switch_inline_query_chosen_chat = None
        if 'switch_inline_query_chosen_chat' in kwargs:
            self.switch_inline_query_chosen_chat = kwargs['switch_inline_query_chosen_chat']
        self._copy_text = None
        if 'copy_text' in kwargs:
            self.copy_text = kwargs['copy_text']
        self._callback_game = None
        if 'callback_game' in kwargs:
            self.callback_game = kwargs['callback_game']
        self._pay = None
        if 'pay' in kwargs:
            self.pay = kwargs['pay']

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._text = value

    @property
    def url(self) -> str | None:
        return self._url

    @url.setter
    def url(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._url = value

    @property
    def callback_data(self) -> str | None:
        return self._callback_data

    @callback_data.setter
    def callback_data(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._callback_data = value

    @property
    def web_app(self) -> WebAppInfo | None:
        return self._web_app

    @web_app.setter
    def web_app(self, value: WebAppInfo | None) -> None:
        TypeChecker.check(value, 'WebAppInfo | None')
        self._web_app = value

    @property
    def login_url(self) -> LoginUrl | None:
        return self._login_url

    @login_url.setter
    def login_url(self, value: LoginUrl | None) -> None:
        TypeChecker.check(value, 'LoginUrl | None')
        self._login_url = value

    @property
    def switch_inline_query(self) -> str | None:
        return self._switch_inline_query

    @switch_inline_query.setter
    def switch_inline_query(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._switch_inline_query = value

    @property
    def switch_inline_query_current_chat(self) -> str | None:
        return self._switch_inline_query_current_chat

    @switch_inline_query_current_chat.setter
    def switch_inline_query_current_chat(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._switch_inline_query_current_chat = value

    @property
    def switch_inline_query_chosen_chat(self) -> SwitchInlineQueryChosenChat | None:
        return self._switch_inline_query_chosen_chat

    @switch_inline_query_chosen_chat.setter
    def switch_inline_query_chosen_chat(self, value: SwitchInlineQueryChosenChat | None) -> None:
        TypeChecker.check(value, 'SwitchInlineQueryChosenChat | None')
        self._switch_inline_query_chosen_chat = value

    @property
    def copy_text(self) -> CopyTextButton | None:
        return self._copy_text

    @copy_text.setter
    def copy_text(self, value: CopyTextButton | None) -> None:
        TypeChecker.check(value, 'CopyTextButton | None')
        self._copy_text = value

    @property
    def callback_game(self) -> CallbackGame | None:
        return self._callback_game

    @callback_game.setter
    def callback_game(self, value: CallbackGame | None) -> None:
        TypeChecker.check(value, 'CallbackGame | None')
        self._callback_game = value

    @property
    def pay(self) -> bool | None:
        return self._pay

    @pay.setter
    def pay(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._pay = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'text': self._text,
            'url': self._url,
            'callback_data': self._callback_data,
            'web_app': self._web_app,
            'login_url': self._login_url,
            'switch_inline_query': self._switch_inline_query,
            'switch_inline_query_current_chat': self._switch_inline_query_current_chat,
            'switch_inline_query_chosen_chat': self._switch_inline_query_chosen_chat,
            'copy_text': self._copy_text,
            'callback_game': self._callback_game,
            'pay': self._pay,
        }

class LoginUrl:
    """This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in: Telegram apps support these buttons as of version 5.7."""
    def __init__(self, **kwargs: Any):
        self._url = None
        if 'url' in kwargs:
            self.url = kwargs['url']
        self._forward_text = None
        if 'forward_text' in kwargs:
            self.forward_text = kwargs['forward_text']
        self._bot_username = None
        if 'bot_username' in kwargs:
            self.bot_username = kwargs['bot_username']
        self._request_write_access = None
        if 'request_write_access' in kwargs:
            self.request_write_access = kwargs['request_write_access']

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._url = value

    @property
    def forward_text(self) -> str | None:
        return self._forward_text

    @forward_text.setter
    def forward_text(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._forward_text = value

    @property
    def bot_username(self) -> str | None:
        return self._bot_username

    @bot_username.setter
    def bot_username(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._bot_username = value

    @property
    def request_write_access(self) -> bool | None:
        return self._request_write_access

    @request_write_access.setter
    def request_write_access(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._request_write_access = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'url': self._url,
            'forward_text': self._forward_text,
            'bot_username': self._bot_username,
            'request_write_access': self._request_write_access,
        }

class SwitchInlineQueryChosenChat:
    """This object represents an inline button that switches the current user to inline mode in a chosen chat, with an optional default inline query."""
    def __init__(self, **kwargs: Any):
        self._query = None
        if 'query' in kwargs:
            self.query = kwargs['query']
        self._allow_user_chats = None
        if 'allow_user_chats' in kwargs:
            self.allow_user_chats = kwargs['allow_user_chats']
        self._allow_bot_chats = None
        if 'allow_bot_chats' in kwargs:
            self.allow_bot_chats = kwargs['allow_bot_chats']
        self._allow_group_chats = None
        if 'allow_group_chats' in kwargs:
            self.allow_group_chats = kwargs['allow_group_chats']
        self._allow_channel_chats = None
        if 'allow_channel_chats' in kwargs:
            self.allow_channel_chats = kwargs['allow_channel_chats']

    @property
    def query(self) -> str | None:
        return self._query

    @query.setter
    def query(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._query = value

    @property
    def allow_user_chats(self) -> bool | None:
        return self._allow_user_chats

    @allow_user_chats.setter
    def allow_user_chats(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._allow_user_chats = value

    @property
    def allow_bot_chats(self) -> bool | None:
        return self._allow_bot_chats

    @allow_bot_chats.setter
    def allow_bot_chats(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._allow_bot_chats = value

    @property
    def allow_group_chats(self) -> bool | None:
        return self._allow_group_chats

    @allow_group_chats.setter
    def allow_group_chats(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._allow_group_chats = value

    @property
    def allow_channel_chats(self) -> bool | None:
        return self._allow_channel_chats

    @allow_channel_chats.setter
    def allow_channel_chats(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._allow_channel_chats = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'query': self._query,
            'allow_user_chats': self._allow_user_chats,
            'allow_bot_chats': self._allow_bot_chats,
            'allow_group_chats': self._allow_group_chats,
            'allow_channel_chats': self._allow_channel_chats,
        }

class CopyTextButton:
    """This object represents an inline keyboard button that copies specified text to the clipboard."""
    def __init__(self, **kwargs: Any):
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._text = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'text': self._text,
        }

class CallbackQuery:
    """This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present."""
    def __init__(self, **kwargs: Any):
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']
        self._from_user = None
        if 'from_user' in kwargs:
            self.from_user = kwargs['from_user']
        self._message = None
        if 'message' in kwargs:
            self.message = kwargs['message']
        self._inline_message_id = None
        if 'inline_message_id' in kwargs:
            self.inline_message_id = kwargs['inline_message_id']
        self._chat_instance = None
        if 'chat_instance' in kwargs:
            self.chat_instance = kwargs['chat_instance']
        self._data = None
        if 'data' in kwargs:
            self.data = kwargs['data']
        self._game_short_name = None
        if 'game_short_name' in kwargs:
            self.game_short_name = kwargs['game_short_name']

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._id = value

    @property
    def from_user(self) -> User:
        return self._from_user

    @from_user.setter
    def from_user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._from_user = value

    @property
    def message(self) -> MaybeInaccessibleMessage | None:
        return self._message

    @message.setter
    def message(self, value: MaybeInaccessibleMessage | None) -> None:
        TypeChecker.check(value, 'MaybeInaccessibleMessage | None')
        self._message = value

    @property
    def inline_message_id(self) -> str | None:
        return self._inline_message_id

    @inline_message_id.setter
    def inline_message_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._inline_message_id = value

    @property
    def chat_instance(self) -> str:
        return self._chat_instance

    @chat_instance.setter
    def chat_instance(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._chat_instance = value

    @property
    def data(self) -> str | None:
        return self._data

    @data.setter
    def data(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._data = value

    @property
    def game_short_name(self) -> str | None:
        return self._game_short_name

    @game_short_name.setter
    def game_short_name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._game_short_name = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'from_user': self._from_user,
            'message': self._message,
            'inline_message_id': self._inline_message_id,
            'chat_instance': self._chat_instance,
            'data': self._data,
            'game_short_name': self._game_short_name,
        }

class ForceReply:
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode. Not supported in channels and for messages sent on behalf of a Telegram Business account."""
    def __init__(self, **kwargs: Any):
        self._force_reply = None
        if 'force_reply' in kwargs:
            self.force_reply = kwargs['force_reply']
        self._input_field_placeholder = None
        if 'input_field_placeholder' in kwargs:
            self.input_field_placeholder = kwargs['input_field_placeholder']
        self._selective = None
        if 'selective' in kwargs:
            self.selective = kwargs['selective']

    @property
    def force_reply(self) -> bool:
        return self._force_reply

    @force_reply.setter
    def force_reply(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._force_reply = value

    @property
    def input_field_placeholder(self) -> str | None:
        return self._input_field_placeholder

    @input_field_placeholder.setter
    def input_field_placeholder(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._input_field_placeholder = value

    @property
    def selective(self) -> bool | None:
        return self._selective

    @selective.setter
    def selective(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._selective = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'force_reply': self._force_reply,
            'input_field_placeholder': self._input_field_placeholder,
            'selective': self._selective,
        }

class ChatPhoto:
    """This object represents a chat photo."""
    def __init__(self, **kwargs: Any):
        self._small_file_id = None
        if 'small_file_id' in kwargs:
            self.small_file_id = kwargs['small_file_id']
        self._small_file_unique_id = None
        if 'small_file_unique_id' in kwargs:
            self.small_file_unique_id = kwargs['small_file_unique_id']
        self._big_file_id = None
        if 'big_file_id' in kwargs:
            self.big_file_id = kwargs['big_file_id']
        self._big_file_unique_id = None
        if 'big_file_unique_id' in kwargs:
            self.big_file_unique_id = kwargs['big_file_unique_id']

    @property
    def small_file_id(self) -> str:
        return self._small_file_id

    @small_file_id.setter
    def small_file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._small_file_id = value

    @property
    def small_file_unique_id(self) -> str:
        return self._small_file_unique_id

    @small_file_unique_id.setter
    def small_file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._small_file_unique_id = value

    @property
    def big_file_id(self) -> str:
        return self._big_file_id

    @big_file_id.setter
    def big_file_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._big_file_id = value

    @property
    def big_file_unique_id(self) -> str:
        return self._big_file_unique_id

    @big_file_unique_id.setter
    def big_file_unique_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._big_file_unique_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'small_file_id': self._small_file_id,
            'small_file_unique_id': self._small_file_unique_id,
            'big_file_id': self._big_file_id,
            'big_file_unique_id': self._big_file_unique_id,
        }

class ChatInviteLink:
    """Represents an invite link for a chat."""
    def __init__(self, **kwargs: Any):
        self._invite_link = None
        if 'invite_link' in kwargs:
            self.invite_link = kwargs['invite_link']
        self._creator = None
        if 'creator' in kwargs:
            self.creator = kwargs['creator']
        self._creates_join_request = None
        if 'creates_join_request' in kwargs:
            self.creates_join_request = kwargs['creates_join_request']
        self._is_primary = None
        if 'is_primary' in kwargs:
            self.is_primary = kwargs['is_primary']
        self._is_revoked = None
        if 'is_revoked' in kwargs:
            self.is_revoked = kwargs['is_revoked']
        self._name = None
        if 'name' in kwargs:
            self.name = kwargs['name']
        self._expire_date = None
        if 'expire_date' in kwargs:
            self.expire_date = kwargs['expire_date']
        self._member_limit = None
        if 'member_limit' in kwargs:
            self.member_limit = kwargs['member_limit']
        self._pending_join_request_count = None
        if 'pending_join_request_count' in kwargs:
            self.pending_join_request_count = kwargs['pending_join_request_count']
        self._subscription_period = None
        if 'subscription_period' in kwargs:
            self.subscription_period = kwargs['subscription_period']
        self._subscription_price = None
        if 'subscription_price' in kwargs:
            self.subscription_price = kwargs['subscription_price']

    @property
    def invite_link(self) -> str:
        return self._invite_link

    @invite_link.setter
    def invite_link(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._invite_link = value

    @property
    def creator(self) -> User:
        return self._creator

    @creator.setter
    def creator(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._creator = value

    @property
    def creates_join_request(self) -> bool:
        return self._creates_join_request

    @creates_join_request.setter
    def creates_join_request(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._creates_join_request = value

    @property
    def is_primary(self) -> bool:
        return self._is_primary

    @is_primary.setter
    def is_primary(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_primary = value

    @property
    def is_revoked(self) -> bool:
        return self._is_revoked

    @is_revoked.setter
    def is_revoked(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_revoked = value

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._name = value

    @property
    def expire_date(self) -> int | None:
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._expire_date = value

    @property
    def member_limit(self) -> int | None:
        return self._member_limit

    @member_limit.setter
    def member_limit(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._member_limit = value

    @property
    def pending_join_request_count(self) -> int | None:
        return self._pending_join_request_count

    @pending_join_request_count.setter
    def pending_join_request_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._pending_join_request_count = value

    @property
    def subscription_period(self) -> int | None:
        return self._subscription_period

    @subscription_period.setter
    def subscription_period(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._subscription_period = value

    @property
    def subscription_price(self) -> int | None:
        return self._subscription_price

    @subscription_price.setter
    def subscription_price(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._subscription_price = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'invite_link': self._invite_link,
            'creator': self._creator,
            'creates_join_request': self._creates_join_request,
            'is_primary': self._is_primary,
            'is_revoked': self._is_revoked,
            'name': self._name,
            'expire_date': self._expire_date,
            'member_limit': self._member_limit,
            'pending_join_request_count': self._pending_join_request_count,
            'subscription_period': self._subscription_period,
            'subscription_price': self._subscription_price,
        }

class ChatAdministratorRights:
    """Represents the rights of an administrator in a chat."""
    def __init__(self, **kwargs: Any):
        self._is_anonymous = None
        if 'is_anonymous' in kwargs:
            self.is_anonymous = kwargs['is_anonymous']
        self._can_manage_chat = None
        if 'can_manage_chat' in kwargs:
            self.can_manage_chat = kwargs['can_manage_chat']
        self._can_delete_messages = None
        if 'can_delete_messages' in kwargs:
            self.can_delete_messages = kwargs['can_delete_messages']
        self._can_manage_video_chats = None
        if 'can_manage_video_chats' in kwargs:
            self.can_manage_video_chats = kwargs['can_manage_video_chats']
        self._can_restrict_members = None
        if 'can_restrict_members' in kwargs:
            self.can_restrict_members = kwargs['can_restrict_members']
        self._can_promote_members = None
        if 'can_promote_members' in kwargs:
            self.can_promote_members = kwargs['can_promote_members']
        self._can_change_info = None
        if 'can_change_info' in kwargs:
            self.can_change_info = kwargs['can_change_info']
        self._can_invite_users = None
        if 'can_invite_users' in kwargs:
            self.can_invite_users = kwargs['can_invite_users']
        self._can_post_stories = None
        if 'can_post_stories' in kwargs:
            self.can_post_stories = kwargs['can_post_stories']
        self._can_edit_stories = None
        if 'can_edit_stories' in kwargs:
            self.can_edit_stories = kwargs['can_edit_stories']
        self._can_delete_stories = None
        if 'can_delete_stories' in kwargs:
            self.can_delete_stories = kwargs['can_delete_stories']
        self._can_post_messages = None
        if 'can_post_messages' in kwargs:
            self.can_post_messages = kwargs['can_post_messages']
        self._can_edit_messages = None
        if 'can_edit_messages' in kwargs:
            self.can_edit_messages = kwargs['can_edit_messages']
        self._can_pin_messages = None
        if 'can_pin_messages' in kwargs:
            self.can_pin_messages = kwargs['can_pin_messages']
        self._can_manage_topics = None
        if 'can_manage_topics' in kwargs:
            self.can_manage_topics = kwargs['can_manage_topics']

    @property
    def is_anonymous(self) -> bool:
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_anonymous = value

    @property
    def can_manage_chat(self) -> bool:
        return self._can_manage_chat

    @can_manage_chat.setter
    def can_manage_chat(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_manage_chat = value

    @property
    def can_delete_messages(self) -> bool:
        return self._can_delete_messages

    @can_delete_messages.setter
    def can_delete_messages(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_delete_messages = value

    @property
    def can_manage_video_chats(self) -> bool:
        return self._can_manage_video_chats

    @can_manage_video_chats.setter
    def can_manage_video_chats(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_manage_video_chats = value

    @property
    def can_restrict_members(self) -> bool:
        return self._can_restrict_members

    @can_restrict_members.setter
    def can_restrict_members(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_restrict_members = value

    @property
    def can_promote_members(self) -> bool:
        return self._can_promote_members

    @can_promote_members.setter
    def can_promote_members(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_promote_members = value

    @property
    def can_change_info(self) -> bool:
        return self._can_change_info

    @can_change_info.setter
    def can_change_info(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_change_info = value

    @property
    def can_invite_users(self) -> bool:
        return self._can_invite_users

    @can_invite_users.setter
    def can_invite_users(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_invite_users = value

    @property
    def can_post_stories(self) -> bool:
        return self._can_post_stories

    @can_post_stories.setter
    def can_post_stories(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_post_stories = value

    @property
    def can_edit_stories(self) -> bool:
        return self._can_edit_stories

    @can_edit_stories.setter
    def can_edit_stories(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_edit_stories = value

    @property
    def can_delete_stories(self) -> bool:
        return self._can_delete_stories

    @can_delete_stories.setter
    def can_delete_stories(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_delete_stories = value

    @property
    def can_post_messages(self) -> bool | None:
        return self._can_post_messages

    @can_post_messages.setter
    def can_post_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_post_messages = value

    @property
    def can_edit_messages(self) -> bool | None:
        return self._can_edit_messages

    @can_edit_messages.setter
    def can_edit_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_edit_messages = value

    @property
    def can_pin_messages(self) -> bool | None:
        return self._can_pin_messages

    @can_pin_messages.setter
    def can_pin_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_pin_messages = value

    @property
    def can_manage_topics(self) -> bool | None:
        return self._can_manage_topics

    @can_manage_topics.setter
    def can_manage_topics(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_manage_topics = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'is_anonymous': self._is_anonymous,
            'can_manage_chat': self._can_manage_chat,
            'can_delete_messages': self._can_delete_messages,
            'can_manage_video_chats': self._can_manage_video_chats,
            'can_restrict_members': self._can_restrict_members,
            'can_promote_members': self._can_promote_members,
            'can_change_info': self._can_change_info,
            'can_invite_users': self._can_invite_users,
            'can_post_stories': self._can_post_stories,
            'can_edit_stories': self._can_edit_stories,
            'can_delete_stories': self._can_delete_stories,
            'can_post_messages': self._can_post_messages,
            'can_edit_messages': self._can_edit_messages,
            'can_pin_messages': self._can_pin_messages,
            'can_manage_topics': self._can_manage_topics,
        }

class ChatMemberUpdated:
    """This object represents changes in the status of a chat member."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._from_user = None
        if 'from_user' in kwargs:
            self.from_user = kwargs['from_user']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._old_chat_member = None
        if 'old_chat_member' in kwargs:
            self.old_chat_member = kwargs['old_chat_member']
        self._new_chat_member = None
        if 'new_chat_member' in kwargs:
            self.new_chat_member = kwargs['new_chat_member']
        self._invite_link = None
        if 'invite_link' in kwargs:
            self.invite_link = kwargs['invite_link']
        self._via_join_request = None
        if 'via_join_request' in kwargs:
            self.via_join_request = kwargs['via_join_request']
        self._via_chat_folder_invite_link = None
        if 'via_chat_folder_invite_link' in kwargs:
            self.via_chat_folder_invite_link = kwargs['via_chat_folder_invite_link']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def from_user(self) -> User:
        return self._from_user

    @from_user.setter
    def from_user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._from_user = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def old_chat_member(self) -> ChatMember:
        return self._old_chat_member

    @old_chat_member.setter
    def old_chat_member(self, value: ChatMember) -> None:
        TypeChecker.check(value, 'ChatMember')
        self._old_chat_member = value

    @property
    def new_chat_member(self) -> ChatMember:
        return self._new_chat_member

    @new_chat_member.setter
    def new_chat_member(self, value: ChatMember) -> None:
        TypeChecker.check(value, 'ChatMember')
        self._new_chat_member = value

    @property
    def invite_link(self) -> ChatInviteLink | None:
        return self._invite_link

    @invite_link.setter
    def invite_link(self, value: ChatInviteLink | None) -> None:
        TypeChecker.check(value, 'ChatInviteLink | None')
        self._invite_link = value

    @property
    def via_join_request(self) -> bool | None:
        return self._via_join_request

    @via_join_request.setter
    def via_join_request(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._via_join_request = value

    @property
    def via_chat_folder_invite_link(self) -> bool | None:
        return self._via_chat_folder_invite_link

    @via_chat_folder_invite_link.setter
    def via_chat_folder_invite_link(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._via_chat_folder_invite_link = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'from_user': self._from_user,
            'date': self._date,
            'old_chat_member': self._old_chat_member,
            'new_chat_member': self._new_chat_member,
            'invite_link': self._invite_link,
            'via_join_request': self._via_join_request,
            'via_chat_folder_invite_link': self._via_chat_folder_invite_link,
        }

class ChatMember:
    """This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class ChatMemberOwner:
    """Represents a chat member that owns the chat and has all administrator privileges."""
    def __init__(self, **kwargs: Any):
        self._status = None
        if 'status' in kwargs:
            self.status = kwargs['status']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._is_anonymous = None
        if 'is_anonymous' in kwargs:
            self.is_anonymous = kwargs['is_anonymous']
        self._custom_title = None
        if 'custom_title' in kwargs:
            self.custom_title = kwargs['custom_title']

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._status = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    @property
    def is_anonymous(self) -> bool:
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_anonymous = value

    @property
    def custom_title(self) -> str | None:
        return self._custom_title

    @custom_title.setter
    def custom_title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._custom_title = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self._status,
            'user': self._user,
            'is_anonymous': self._is_anonymous,
            'custom_title': self._custom_title,
        }

class ChatMemberAdministrator:
    """Represents a chat member that has some additional privileges."""
    def __init__(self, **kwargs: Any):
        self._status = None
        if 'status' in kwargs:
            self.status = kwargs['status']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._can_be_edited = None
        if 'can_be_edited' in kwargs:
            self.can_be_edited = kwargs['can_be_edited']
        self._is_anonymous = None
        if 'is_anonymous' in kwargs:
            self.is_anonymous = kwargs['is_anonymous']
        self._can_manage_chat = None
        if 'can_manage_chat' in kwargs:
            self.can_manage_chat = kwargs['can_manage_chat']
        self._can_delete_messages = None
        if 'can_delete_messages' in kwargs:
            self.can_delete_messages = kwargs['can_delete_messages']
        self._can_manage_video_chats = None
        if 'can_manage_video_chats' in kwargs:
            self.can_manage_video_chats = kwargs['can_manage_video_chats']
        self._can_restrict_members = None
        if 'can_restrict_members' in kwargs:
            self.can_restrict_members = kwargs['can_restrict_members']
        self._can_promote_members = None
        if 'can_promote_members' in kwargs:
            self.can_promote_members = kwargs['can_promote_members']
        self._can_change_info = None
        if 'can_change_info' in kwargs:
            self.can_change_info = kwargs['can_change_info']
        self._can_invite_users = None
        if 'can_invite_users' in kwargs:
            self.can_invite_users = kwargs['can_invite_users']
        self._can_post_stories = None
        if 'can_post_stories' in kwargs:
            self.can_post_stories = kwargs['can_post_stories']
        self._can_edit_stories = None
        if 'can_edit_stories' in kwargs:
            self.can_edit_stories = kwargs['can_edit_stories']
        self._can_delete_stories = None
        if 'can_delete_stories' in kwargs:
            self.can_delete_stories = kwargs['can_delete_stories']
        self._can_post_messages = None
        if 'can_post_messages' in kwargs:
            self.can_post_messages = kwargs['can_post_messages']
        self._can_edit_messages = None
        if 'can_edit_messages' in kwargs:
            self.can_edit_messages = kwargs['can_edit_messages']
        self._can_pin_messages = None
        if 'can_pin_messages' in kwargs:
            self.can_pin_messages = kwargs['can_pin_messages']
        self._can_manage_topics = None
        if 'can_manage_topics' in kwargs:
            self.can_manage_topics = kwargs['can_manage_topics']
        self._custom_title = None
        if 'custom_title' in kwargs:
            self.custom_title = kwargs['custom_title']

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._status = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    @property
    def can_be_edited(self) -> bool:
        return self._can_be_edited

    @can_be_edited.setter
    def can_be_edited(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_be_edited = value

    @property
    def is_anonymous(self) -> bool:
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_anonymous = value

    @property
    def can_manage_chat(self) -> bool:
        return self._can_manage_chat

    @can_manage_chat.setter
    def can_manage_chat(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_manage_chat = value

    @property
    def can_delete_messages(self) -> bool:
        return self._can_delete_messages

    @can_delete_messages.setter
    def can_delete_messages(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_delete_messages = value

    @property
    def can_manage_video_chats(self) -> bool:
        return self._can_manage_video_chats

    @can_manage_video_chats.setter
    def can_manage_video_chats(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_manage_video_chats = value

    @property
    def can_restrict_members(self) -> bool:
        return self._can_restrict_members

    @can_restrict_members.setter
    def can_restrict_members(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_restrict_members = value

    @property
    def can_promote_members(self) -> bool:
        return self._can_promote_members

    @can_promote_members.setter
    def can_promote_members(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_promote_members = value

    @property
    def can_change_info(self) -> bool:
        return self._can_change_info

    @can_change_info.setter
    def can_change_info(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_change_info = value

    @property
    def can_invite_users(self) -> bool:
        return self._can_invite_users

    @can_invite_users.setter
    def can_invite_users(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_invite_users = value

    @property
    def can_post_stories(self) -> bool:
        return self._can_post_stories

    @can_post_stories.setter
    def can_post_stories(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_post_stories = value

    @property
    def can_edit_stories(self) -> bool:
        return self._can_edit_stories

    @can_edit_stories.setter
    def can_edit_stories(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_edit_stories = value

    @property
    def can_delete_stories(self) -> bool:
        return self._can_delete_stories

    @can_delete_stories.setter
    def can_delete_stories(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_delete_stories = value

    @property
    def can_post_messages(self) -> bool | None:
        return self._can_post_messages

    @can_post_messages.setter
    def can_post_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_post_messages = value

    @property
    def can_edit_messages(self) -> bool | None:
        return self._can_edit_messages

    @can_edit_messages.setter
    def can_edit_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_edit_messages = value

    @property
    def can_pin_messages(self) -> bool | None:
        return self._can_pin_messages

    @can_pin_messages.setter
    def can_pin_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_pin_messages = value

    @property
    def can_manage_topics(self) -> bool | None:
        return self._can_manage_topics

    @can_manage_topics.setter
    def can_manage_topics(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_manage_topics = value

    @property
    def custom_title(self) -> str | None:
        return self._custom_title

    @custom_title.setter
    def custom_title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._custom_title = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self._status,
            'user': self._user,
            'can_be_edited': self._can_be_edited,
            'is_anonymous': self._is_anonymous,
            'can_manage_chat': self._can_manage_chat,
            'can_delete_messages': self._can_delete_messages,
            'can_manage_video_chats': self._can_manage_video_chats,
            'can_restrict_members': self._can_restrict_members,
            'can_promote_members': self._can_promote_members,
            'can_change_info': self._can_change_info,
            'can_invite_users': self._can_invite_users,
            'can_post_stories': self._can_post_stories,
            'can_edit_stories': self._can_edit_stories,
            'can_delete_stories': self._can_delete_stories,
            'can_post_messages': self._can_post_messages,
            'can_edit_messages': self._can_edit_messages,
            'can_pin_messages': self._can_pin_messages,
            'can_manage_topics': self._can_manage_topics,
            'custom_title': self._custom_title,
        }

class ChatMemberMember:
    """Represents a chat member that has no additional privileges or restrictions."""
    def __init__(self, **kwargs: Any):
        self._status = None
        if 'status' in kwargs:
            self.status = kwargs['status']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._until_date = None
        if 'until_date' in kwargs:
            self.until_date = kwargs['until_date']

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._status = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    @property
    def until_date(self) -> int | None:
        return self._until_date

    @until_date.setter
    def until_date(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._until_date = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self._status,
            'user': self._user,
            'until_date': self._until_date,
        }

class ChatMemberRestricted:
    """Represents a chat member that is under certain restrictions in the chat. Supergroups only."""
    def __init__(self, **kwargs: Any):
        self._status = None
        if 'status' in kwargs:
            self.status = kwargs['status']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._is_member = None
        if 'is_member' in kwargs:
            self.is_member = kwargs['is_member']
        self._can_send_messages = None
        if 'can_send_messages' in kwargs:
            self.can_send_messages = kwargs['can_send_messages']
        self._can_send_audios = None
        if 'can_send_audios' in kwargs:
            self.can_send_audios = kwargs['can_send_audios']
        self._can_send_documents = None
        if 'can_send_documents' in kwargs:
            self.can_send_documents = kwargs['can_send_documents']
        self._can_send_photos = None
        if 'can_send_photos' in kwargs:
            self.can_send_photos = kwargs['can_send_photos']
        self._can_send_videos = None
        if 'can_send_videos' in kwargs:
            self.can_send_videos = kwargs['can_send_videos']
        self._can_send_video_notes = None
        if 'can_send_video_notes' in kwargs:
            self.can_send_video_notes = kwargs['can_send_video_notes']
        self._can_send_voice_notes = None
        if 'can_send_voice_notes' in kwargs:
            self.can_send_voice_notes = kwargs['can_send_voice_notes']
        self._can_send_polls = None
        if 'can_send_polls' in kwargs:
            self.can_send_polls = kwargs['can_send_polls']
        self._can_send_other_messages = None
        if 'can_send_other_messages' in kwargs:
            self.can_send_other_messages = kwargs['can_send_other_messages']
        self._can_add_web_page_previews = None
        if 'can_add_web_page_previews' in kwargs:
            self.can_add_web_page_previews = kwargs['can_add_web_page_previews']
        self._can_change_info = None
        if 'can_change_info' in kwargs:
            self.can_change_info = kwargs['can_change_info']
        self._can_invite_users = None
        if 'can_invite_users' in kwargs:
            self.can_invite_users = kwargs['can_invite_users']
        self._can_pin_messages = None
        if 'can_pin_messages' in kwargs:
            self.can_pin_messages = kwargs['can_pin_messages']
        self._can_manage_topics = None
        if 'can_manage_topics' in kwargs:
            self.can_manage_topics = kwargs['can_manage_topics']
        self._until_date = None
        if 'until_date' in kwargs:
            self.until_date = kwargs['until_date']

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._status = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    @property
    def is_member(self) -> bool:
        return self._is_member

    @is_member.setter
    def is_member(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_member = value

    @property
    def can_send_messages(self) -> bool:
        return self._can_send_messages

    @can_send_messages.setter
    def can_send_messages(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_messages = value

    @property
    def can_send_audios(self) -> bool:
        return self._can_send_audios

    @can_send_audios.setter
    def can_send_audios(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_audios = value

    @property
    def can_send_documents(self) -> bool:
        return self._can_send_documents

    @can_send_documents.setter
    def can_send_documents(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_documents = value

    @property
    def can_send_photos(self) -> bool:
        return self._can_send_photos

    @can_send_photos.setter
    def can_send_photos(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_photos = value

    @property
    def can_send_videos(self) -> bool:
        return self._can_send_videos

    @can_send_videos.setter
    def can_send_videos(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_videos = value

    @property
    def can_send_video_notes(self) -> bool:
        return self._can_send_video_notes

    @can_send_video_notes.setter
    def can_send_video_notes(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_video_notes = value

    @property
    def can_send_voice_notes(self) -> bool:
        return self._can_send_voice_notes

    @can_send_voice_notes.setter
    def can_send_voice_notes(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_voice_notes = value

    @property
    def can_send_polls(self) -> bool:
        return self._can_send_polls

    @can_send_polls.setter
    def can_send_polls(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_polls = value

    @property
    def can_send_other_messages(self) -> bool:
        return self._can_send_other_messages

    @can_send_other_messages.setter
    def can_send_other_messages(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_send_other_messages = value

    @property
    def can_add_web_page_previews(self) -> bool:
        return self._can_add_web_page_previews

    @can_add_web_page_previews.setter
    def can_add_web_page_previews(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_add_web_page_previews = value

    @property
    def can_change_info(self) -> bool:
        return self._can_change_info

    @can_change_info.setter
    def can_change_info(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_change_info = value

    @property
    def can_invite_users(self) -> bool:
        return self._can_invite_users

    @can_invite_users.setter
    def can_invite_users(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_invite_users = value

    @property
    def can_pin_messages(self) -> bool:
        return self._can_pin_messages

    @can_pin_messages.setter
    def can_pin_messages(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_pin_messages = value

    @property
    def can_manage_topics(self) -> bool:
        return self._can_manage_topics

    @can_manage_topics.setter
    def can_manage_topics(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_manage_topics = value

    @property
    def until_date(self) -> int:
        return self._until_date

    @until_date.setter
    def until_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._until_date = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self._status,
            'user': self._user,
            'is_member': self._is_member,
            'can_send_messages': self._can_send_messages,
            'can_send_audios': self._can_send_audios,
            'can_send_documents': self._can_send_documents,
            'can_send_photos': self._can_send_photos,
            'can_send_videos': self._can_send_videos,
            'can_send_video_notes': self._can_send_video_notes,
            'can_send_voice_notes': self._can_send_voice_notes,
            'can_send_polls': self._can_send_polls,
            'can_send_other_messages': self._can_send_other_messages,
            'can_add_web_page_previews': self._can_add_web_page_previews,
            'can_change_info': self._can_change_info,
            'can_invite_users': self._can_invite_users,
            'can_pin_messages': self._can_pin_messages,
            'can_manage_topics': self._can_manage_topics,
            'until_date': self._until_date,
        }

class ChatMemberLeft:
    """Represents a chat member that isn't currently a member of the chat, but may join it themselves."""
    def __init__(self, **kwargs: Any):
        self._status = None
        if 'status' in kwargs:
            self.status = kwargs['status']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._status = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self._status,
            'user': self._user,
        }

class ChatMemberBanned:
    """Represents a chat member that was banned in the chat and can't return to the chat or view chat messages."""
    def __init__(self, **kwargs: Any):
        self._status = None
        if 'status' in kwargs:
            self.status = kwargs['status']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._until_date = None
        if 'until_date' in kwargs:
            self.until_date = kwargs['until_date']

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._status = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    @property
    def until_date(self) -> int:
        return self._until_date

    @until_date.setter
    def until_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._until_date = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'status': self._status,
            'user': self._user,
            'until_date': self._until_date,
        }

class ChatJoinRequest:
    """Represents a join request sent to a chat."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._from_user = None
        if 'from_user' in kwargs:
            self.from_user = kwargs['from_user']
        self._user_chat_id = None
        if 'user_chat_id' in kwargs:
            self.user_chat_id = kwargs['user_chat_id']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._bio = None
        if 'bio' in kwargs:
            self.bio = kwargs['bio']
        self._invite_link = None
        if 'invite_link' in kwargs:
            self.invite_link = kwargs['invite_link']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def from_user(self) -> User:
        return self._from_user

    @from_user.setter
    def from_user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._from_user = value

    @property
    def user_chat_id(self) -> int:
        return self._user_chat_id

    @user_chat_id.setter
    def user_chat_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._user_chat_id = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def bio(self) -> str | None:
        return self._bio

    @bio.setter
    def bio(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._bio = value

    @property
    def invite_link(self) -> ChatInviteLink | None:
        return self._invite_link

    @invite_link.setter
    def invite_link(self, value: ChatInviteLink | None) -> None:
        TypeChecker.check(value, 'ChatInviteLink | None')
        self._invite_link = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'from_user': self._from_user,
            'user_chat_id': self._user_chat_id,
            'date': self._date,
            'bio': self._bio,
            'invite_link': self._invite_link,
        }

class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat."""
    def __init__(self, **kwargs: Any):
        self._can_send_messages = None
        if 'can_send_messages' in kwargs:
            self.can_send_messages = kwargs['can_send_messages']
        self._can_send_audios = None
        if 'can_send_audios' in kwargs:
            self.can_send_audios = kwargs['can_send_audios']
        self._can_send_documents = None
        if 'can_send_documents' in kwargs:
            self.can_send_documents = kwargs['can_send_documents']
        self._can_send_photos = None
        if 'can_send_photos' in kwargs:
            self.can_send_photos = kwargs['can_send_photos']
        self._can_send_videos = None
        if 'can_send_videos' in kwargs:
            self.can_send_videos = kwargs['can_send_videos']
        self._can_send_video_notes = None
        if 'can_send_video_notes' in kwargs:
            self.can_send_video_notes = kwargs['can_send_video_notes']
        self._can_send_voice_notes = None
        if 'can_send_voice_notes' in kwargs:
            self.can_send_voice_notes = kwargs['can_send_voice_notes']
        self._can_send_polls = None
        if 'can_send_polls' in kwargs:
            self.can_send_polls = kwargs['can_send_polls']
        self._can_send_other_messages = None
        if 'can_send_other_messages' in kwargs:
            self.can_send_other_messages = kwargs['can_send_other_messages']
        self._can_add_web_page_previews = None
        if 'can_add_web_page_previews' in kwargs:
            self.can_add_web_page_previews = kwargs['can_add_web_page_previews']
        self._can_change_info = None
        if 'can_change_info' in kwargs:
            self.can_change_info = kwargs['can_change_info']
        self._can_invite_users = None
        if 'can_invite_users' in kwargs:
            self.can_invite_users = kwargs['can_invite_users']
        self._can_pin_messages = None
        if 'can_pin_messages' in kwargs:
            self.can_pin_messages = kwargs['can_pin_messages']
        self._can_manage_topics = None
        if 'can_manage_topics' in kwargs:
            self.can_manage_topics = kwargs['can_manage_topics']

    @property
    def can_send_messages(self) -> bool | None:
        return self._can_send_messages

    @can_send_messages.setter
    def can_send_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_messages = value

    @property
    def can_send_audios(self) -> bool | None:
        return self._can_send_audios

    @can_send_audios.setter
    def can_send_audios(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_audios = value

    @property
    def can_send_documents(self) -> bool | None:
        return self._can_send_documents

    @can_send_documents.setter
    def can_send_documents(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_documents = value

    @property
    def can_send_photos(self) -> bool | None:
        return self._can_send_photos

    @can_send_photos.setter
    def can_send_photos(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_photos = value

    @property
    def can_send_videos(self) -> bool | None:
        return self._can_send_videos

    @can_send_videos.setter
    def can_send_videos(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_videos = value

    @property
    def can_send_video_notes(self) -> bool | None:
        return self._can_send_video_notes

    @can_send_video_notes.setter
    def can_send_video_notes(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_video_notes = value

    @property
    def can_send_voice_notes(self) -> bool | None:
        return self._can_send_voice_notes

    @can_send_voice_notes.setter
    def can_send_voice_notes(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_voice_notes = value

    @property
    def can_send_polls(self) -> bool | None:
        return self._can_send_polls

    @can_send_polls.setter
    def can_send_polls(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_polls = value

    @property
    def can_send_other_messages(self) -> bool | None:
        return self._can_send_other_messages

    @can_send_other_messages.setter
    def can_send_other_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_send_other_messages = value

    @property
    def can_add_web_page_previews(self) -> bool | None:
        return self._can_add_web_page_previews

    @can_add_web_page_previews.setter
    def can_add_web_page_previews(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_add_web_page_previews = value

    @property
    def can_change_info(self) -> bool | None:
        return self._can_change_info

    @can_change_info.setter
    def can_change_info(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_change_info = value

    @property
    def can_invite_users(self) -> bool | None:
        return self._can_invite_users

    @can_invite_users.setter
    def can_invite_users(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_invite_users = value

    @property
    def can_pin_messages(self) -> bool | None:
        return self._can_pin_messages

    @can_pin_messages.setter
    def can_pin_messages(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_pin_messages = value

    @property
    def can_manage_topics(self) -> bool | None:
        return self._can_manage_topics

    @can_manage_topics.setter
    def can_manage_topics(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._can_manage_topics = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'can_send_messages': self._can_send_messages,
            'can_send_audios': self._can_send_audios,
            'can_send_documents': self._can_send_documents,
            'can_send_photos': self._can_send_photos,
            'can_send_videos': self._can_send_videos,
            'can_send_video_notes': self._can_send_video_notes,
            'can_send_voice_notes': self._can_send_voice_notes,
            'can_send_polls': self._can_send_polls,
            'can_send_other_messages': self._can_send_other_messages,
            'can_add_web_page_previews': self._can_add_web_page_previews,
            'can_change_info': self._can_change_info,
            'can_invite_users': self._can_invite_users,
            'can_pin_messages': self._can_pin_messages,
            'can_manage_topics': self._can_manage_topics,
        }

class Birthdate:
    """Describes the birthdate of a user."""
    def __init__(self, **kwargs: Any):
        self._day = None
        if 'day' in kwargs:
            self.day = kwargs['day']
        self._month = None
        if 'month' in kwargs:
            self.month = kwargs['month']
        self._year = None
        if 'year' in kwargs:
            self.year = kwargs['year']

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._day = value

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._month = value

    @property
    def year(self) -> int | None:
        return self._year

    @year.setter
    def year(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._year = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'day': self._day,
            'month': self._month,
            'year': self._year,
        }

class BusinessIntro:
    """Contains information about the start page settings of a Telegram Business account."""
    def __init__(self, **kwargs: Any):
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']
        self._message = None
        if 'message' in kwargs:
            self.message = kwargs['message']
        self._sticker = None
        if 'sticker' in kwargs:
            self.sticker = kwargs['sticker']

    @property
    def title(self) -> str | None:
        return self._title

    @title.setter
    def title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._title = value

    @property
    def message(self) -> str | None:
        return self._message

    @message.setter
    def message(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._message = value

    @property
    def sticker(self) -> Sticker | None:
        return self._sticker

    @sticker.setter
    def sticker(self, value: Sticker | None) -> None:
        TypeChecker.check(value, 'Sticker | None')
        self._sticker = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'title': self._title,
            'message': self._message,
            'sticker': self._sticker,
        }

class BusinessLocation:
    """Contains information about the location of a Telegram Business account."""
    def __init__(self, **kwargs: Any):
        self._address = None
        if 'address' in kwargs:
            self.address = kwargs['address']
        self._location = None
        if 'location' in kwargs:
            self.location = kwargs['location']

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._address = value

    @property
    def location(self) -> Location | None:
        return self._location

    @location.setter
    def location(self, value: Location | None) -> None:
        TypeChecker.check(value, 'Location | None')
        self._location = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'address': self._address,
            'location': self._location,
        }

class BusinessOpeningHoursInterval:
    """Describes an interval of time during which a business is open."""
    def __init__(self, **kwargs: Any):
        self._opening_minute = None
        if 'opening_minute' in kwargs:
            self.opening_minute = kwargs['opening_minute']
        self._closing_minute = None
        if 'closing_minute' in kwargs:
            self.closing_minute = kwargs['closing_minute']

    @property
    def opening_minute(self) -> int:
        return self._opening_minute

    @opening_minute.setter
    def opening_minute(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._opening_minute = value

    @property
    def closing_minute(self) -> int:
        return self._closing_minute

    @closing_minute.setter
    def closing_minute(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._closing_minute = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'opening_minute': self._opening_minute,
            'closing_minute': self._closing_minute,
        }

class BusinessOpeningHours:
    """Describes the opening hours of a business."""
    def __init__(self, **kwargs: Any):
        self._time_zone_name = None
        if 'time_zone_name' in kwargs:
            self.time_zone_name = kwargs['time_zone_name']
        self._opening_hours = None
        if 'opening_hours' in kwargs:
            self.opening_hours = kwargs['opening_hours']

    @property
    def time_zone_name(self) -> str:
        return self._time_zone_name

    @time_zone_name.setter
    def time_zone_name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._time_zone_name = value

    @property
    def opening_hours(self) -> List[BusinessOpeningHoursInterval]:
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value: List[BusinessOpeningHoursInterval]) -> None:
        TypeChecker.check(value, 'List[BusinessOpeningHoursInterval]')
        self._opening_hours = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'time_zone_name': self._time_zone_name,
            'opening_hours': self._opening_hours,
        }

class ChatLocation:
    """Represents a location to which a chat is connected."""
    def __init__(self, **kwargs: Any):
        self._location = None
        if 'location' in kwargs:
            self.location = kwargs['location']
        self._address = None
        if 'address' in kwargs:
            self.address = kwargs['address']

    @property
    def location(self) -> Location:
        return self._location

    @location.setter
    def location(self, value: Location) -> None:
        TypeChecker.check(value, 'Location')
        self._location = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._address = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'location': self._location,
            'address': self._address,
        }

class ReactionType:
    """This object describes the type of a reaction. Currently, it can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class ReactionTypeEmoji:
    """The reaction is based on an emoji."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._emoji = None
        if 'emoji' in kwargs:
            self.emoji = kwargs['emoji']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def emoji(self) -> str:
        return self._emoji

    @emoji.setter
    def emoji(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._emoji = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'emoji': self._emoji,
        }

class ReactionTypeCustomEmoji:
    """The reaction is based on a custom emoji."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._custom_emoji_id = None
        if 'custom_emoji_id' in kwargs:
            self.custom_emoji_id = kwargs['custom_emoji_id']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def custom_emoji_id(self) -> str:
        return self._custom_emoji_id

    @custom_emoji_id.setter
    def custom_emoji_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._custom_emoji_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'custom_emoji_id': self._custom_emoji_id,
        }

class ReactionTypePaid:
    """The reaction is paid."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class ReactionCount:
    """Represents a reaction added to a message along with the number of times it was added."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._total_count = None
        if 'total_count' in kwargs:
            self.total_count = kwargs['total_count']

    @property
    def type(self) -> ReactionType:
        return self._type

    @type.setter
    def type(self, value: ReactionType) -> None:
        TypeChecker.check(value, 'ReactionType')
        self._type = value

    @property
    def total_count(self) -> int:
        return self._total_count

    @total_count.setter
    def total_count(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._total_count = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'total_count': self._total_count,
        }

class MessageReactionUpdated:
    """This object represents a change of a reaction on a message performed by a user."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._actor_chat = None
        if 'actor_chat' in kwargs:
            self.actor_chat = kwargs['actor_chat']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._old_reaction = None
        if 'old_reaction' in kwargs:
            self.old_reaction = kwargs['old_reaction']
        self._new_reaction = None
        if 'new_reaction' in kwargs:
            self.new_reaction = kwargs['new_reaction']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    @property
    def user(self) -> User | None:
        return self._user

    @user.setter
    def user(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._user = value

    @property
    def actor_chat(self) -> Chat | None:
        return self._actor_chat

    @actor_chat.setter
    def actor_chat(self, value: Chat | None) -> None:
        TypeChecker.check(value, 'Chat | None')
        self._actor_chat = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def old_reaction(self) -> List[ReactionType]:
        return self._old_reaction

    @old_reaction.setter
    def old_reaction(self, value: List[ReactionType]) -> None:
        TypeChecker.check(value, 'List[ReactionType]')
        self._old_reaction = value

    @property
    def new_reaction(self) -> List[ReactionType]:
        return self._new_reaction

    @new_reaction.setter
    def new_reaction(self, value: List[ReactionType]) -> None:
        TypeChecker.check(value, 'List[ReactionType]')
        self._new_reaction = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'message_id': self._message_id,
            'user': self._user,
            'actor_chat': self._actor_chat,
            'date': self._date,
            'old_reaction': self._old_reaction,
            'new_reaction': self._new_reaction,
        }

class MessageReactionCountUpdated:
    """This object represents reaction changes on a message with anonymous reactions."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._message_id = None
        if 'message_id' in kwargs:
            self.message_id = kwargs['message_id']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._reactions = None
        if 'reactions' in kwargs:
            self.reactions = kwargs['reactions']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def message_id(self) -> int:
        return self._message_id

    @message_id.setter
    def message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_id = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def reactions(self) -> List[ReactionCount]:
        return self._reactions

    @reactions.setter
    def reactions(self, value: List[ReactionCount]) -> None:
        TypeChecker.check(value, 'List[ReactionCount]')
        self._reactions = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'message_id': self._message_id,
            'date': self._date,
            'reactions': self._reactions,
        }

class ForumTopic:
    """This object represents a forum topic."""
    def __init__(self, **kwargs: Any):
        self._message_thread_id = None
        if 'message_thread_id' in kwargs:
            self.message_thread_id = kwargs['message_thread_id']
        self._name = None
        if 'name' in kwargs:
            self.name = kwargs['name']
        self._icon_color = None
        if 'icon_color' in kwargs:
            self.icon_color = kwargs['icon_color']
        self._icon_custom_emoji_id = None
        if 'icon_custom_emoji_id' in kwargs:
            self.icon_custom_emoji_id = kwargs['icon_custom_emoji_id']

    @property
    def message_thread_id(self) -> int:
        return self._message_thread_id

    @message_thread_id.setter
    def message_thread_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._message_thread_id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._name = value

    @property
    def icon_color(self) -> int:
        return self._icon_color

    @icon_color.setter
    def icon_color(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._icon_color = value

    @property
    def icon_custom_emoji_id(self) -> str | None:
        return self._icon_custom_emoji_id

    @icon_custom_emoji_id.setter
    def icon_custom_emoji_id(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._icon_custom_emoji_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'message_thread_id': self._message_thread_id,
            'name': self._name,
            'icon_color': self._icon_color,
            'icon_custom_emoji_id': self._icon_custom_emoji_id,
        }

class BotCommand:
    """This object represents a bot command."""
    def __init__(self, **kwargs: Any):
        self._command = None
        if 'command' in kwargs:
            self.command = kwargs['command']
        self._description = None
        if 'description' in kwargs:
            self.description = kwargs['description']

    @property
    def command(self) -> str:
        return self._command

    @command.setter
    def command(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._command = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._description = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'command': self._command,
            'description': self._description,
        }

class BotCommandScope:
    """This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class BotCommandScopeDefault:
    """Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class BotCommandScopeAllPrivateChats:
    """Represents the scope of bot commands, covering all private chats."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class BotCommandScopeAllGroupChats:
    """Represents the scope of bot commands, covering all group and supergroup chats."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class BotCommandScopeAllChatAdministrators:
    """Represents the scope of bot commands, covering all group and supergroup chat administrators."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class BotCommandScopeChat:
    """Represents the scope of bot commands, covering a specific chat."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._chat_id = None
        if 'chat_id' in kwargs:
            self.chat_id = kwargs['chat_id']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def chat_id(self) -> int | str:
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value: int | str) -> None:
        TypeChecker.check(value, 'int | str')
        self._chat_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'chat_id': self._chat_id,
        }

class BotCommandScopeChatAdministrators:
    """Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._chat_id = None
        if 'chat_id' in kwargs:
            self.chat_id = kwargs['chat_id']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def chat_id(self) -> int | str:
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value: int | str) -> None:
        TypeChecker.check(value, 'int | str')
        self._chat_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'chat_id': self._chat_id,
        }

class BotCommandScopeChatMember:
    """Represents the scope of bot commands, covering a specific member of a group or supergroup chat."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._chat_id = None
        if 'chat_id' in kwargs:
            self.chat_id = kwargs['chat_id']
        self._user_id = None
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def chat_id(self) -> int | str:
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value: int | str) -> None:
        TypeChecker.check(value, 'int | str')
        self._chat_id = value

    @property
    def user_id(self) -> int:
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._user_id = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'chat_id': self._chat_id,
            'user_id': self._user_id,
        }

class BotName:
    """This object represents the bot's name."""
    def __init__(self, **kwargs: Any):
        self._name = None
        if 'name' in kwargs:
            self.name = kwargs['name']

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._name = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self._name,
        }

class BotDescription:
    """This object represents the bot's description."""
    def __init__(self, **kwargs: Any):
        self._description = None
        if 'description' in kwargs:
            self.description = kwargs['description']

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._description = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'description': self._description,
        }

class BotShortDescription:
    """This object represents the bot's short description."""
    def __init__(self, **kwargs: Any):
        self._short_description = None
        if 'short_description' in kwargs:
            self.short_description = kwargs['short_description']

    @property
    def short_description(self) -> str:
        return self._short_description

    @short_description.setter
    def short_description(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._short_description = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'short_description': self._short_description,
        }

class MenuButton:
    """This object describes the bot's menu button in a private chat. It should be one of If a menu button other than MenuButtonDefault is set for a private chat, then it is applied in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot commands."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class MenuButtonCommands:
    """Represents a menu button, which opens the bot's list of commands."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class MenuButtonWebApp:
    """Represents a menu button, which launches a Web App."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._text = None
        if 'text' in kwargs:
            self.text = kwargs['text']
        self._web_app = None
        if 'web_app' in kwargs:
            self.web_app = kwargs['web_app']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._text = value

    @property
    def web_app(self) -> WebAppInfo:
        return self._web_app

    @web_app.setter
    def web_app(self, value: WebAppInfo) -> None:
        TypeChecker.check(value, 'WebAppInfo')
        self._web_app = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'text': self._text,
            'web_app': self._web_app,
        }

class MenuButtonDefault:
    """Describes that no specific value for the menu button was set."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
        }

class ChatBoostSource:
    """This object describes the source of a chat boost. It can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class ChatBoostSourcePremium:
    """The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user."""
    def __init__(self, **kwargs: Any):
        self._source = None
        if 'source' in kwargs:
            self.source = kwargs['source']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._source = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'source': self._source,
            'user': self._user,
        }

class ChatBoostSourceGiftCode:
    """The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription."""
    def __init__(self, **kwargs: Any):
        self._source = None
        if 'source' in kwargs:
            self.source = kwargs['source']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._source = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'source': self._source,
            'user': self._user,
        }

class ChatBoostSourceGiveaway:
    """The boost was obtained by the creation of a Telegram Premium or a Telegram Star giveaway. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and prize_star_count / 500 times for one year for Telegram Star giveaways."""
    def __init__(self, **kwargs: Any):
        self._source = None
        if 'source' in kwargs:
            self.source = kwargs['source']
        self._giveaway_message_id = None
        if 'giveaway_message_id' in kwargs:
            self.giveaway_message_id = kwargs['giveaway_message_id']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._prize_star_count = None
        if 'prize_star_count' in kwargs:
            self.prize_star_count = kwargs['prize_star_count']
        self._is_unclaimed = None
        if 'is_unclaimed' in kwargs:
            self.is_unclaimed = kwargs['is_unclaimed']

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._source = value

    @property
    def giveaway_message_id(self) -> int:
        return self._giveaway_message_id

    @giveaway_message_id.setter
    def giveaway_message_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._giveaway_message_id = value

    @property
    def user(self) -> User | None:
        return self._user

    @user.setter
    def user(self, value: User | None) -> None:
        TypeChecker.check(value, 'User | None')
        self._user = value

    @property
    def prize_star_count(self) -> int | None:
        return self._prize_star_count

    @prize_star_count.setter
    def prize_star_count(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._prize_star_count = value

    @property
    def is_unclaimed(self) -> bool | None:
        return self._is_unclaimed

    @is_unclaimed.setter
    def is_unclaimed(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._is_unclaimed = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'source': self._source,
            'giveaway_message_id': self._giveaway_message_id,
            'user': self._user,
            'prize_star_count': self._prize_star_count,
            'is_unclaimed': self._is_unclaimed,
        }

class ChatBoost:
    """This object contains information about a chat boost."""
    def __init__(self, **kwargs: Any):
        self._boost_id = None
        if 'boost_id' in kwargs:
            self.boost_id = kwargs['boost_id']
        self._add_date = None
        if 'add_date' in kwargs:
            self.add_date = kwargs['add_date']
        self._expiration_date = None
        if 'expiration_date' in kwargs:
            self.expiration_date = kwargs['expiration_date']
        self._source = None
        if 'source' in kwargs:
            self.source = kwargs['source']

    @property
    def boost_id(self) -> str:
        return self._boost_id

    @boost_id.setter
    def boost_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._boost_id = value

    @property
    def add_date(self) -> int:
        return self._add_date

    @add_date.setter
    def add_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._add_date = value

    @property
    def expiration_date(self) -> int:
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._expiration_date = value

    @property
    def source(self) -> ChatBoostSource:
        return self._source

    @source.setter
    def source(self, value: ChatBoostSource) -> None:
        TypeChecker.check(value, 'ChatBoostSource')
        self._source = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'boost_id': self._boost_id,
            'add_date': self._add_date,
            'expiration_date': self._expiration_date,
            'source': self._source,
        }

class ChatBoostUpdated:
    """This object represents a boost added to a chat or changed."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._boost = None
        if 'boost' in kwargs:
            self.boost = kwargs['boost']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def boost(self) -> ChatBoost:
        return self._boost

    @boost.setter
    def boost(self, value: ChatBoost) -> None:
        TypeChecker.check(value, 'ChatBoost')
        self._boost = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'boost': self._boost,
        }

class ChatBoostRemoved:
    """This object represents a boost removed from a chat."""
    def __init__(self, **kwargs: Any):
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._boost_id = None
        if 'boost_id' in kwargs:
            self.boost_id = kwargs['boost_id']
        self._remove_date = None
        if 'remove_date' in kwargs:
            self.remove_date = kwargs['remove_date']
        self._source = None
        if 'source' in kwargs:
            self.source = kwargs['source']

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def boost_id(self) -> str:
        return self._boost_id

    @boost_id.setter
    def boost_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._boost_id = value

    @property
    def remove_date(self) -> int:
        return self._remove_date

    @remove_date.setter
    def remove_date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._remove_date = value

    @property
    def source(self) -> ChatBoostSource:
        return self._source

    @source.setter
    def source(self, value: ChatBoostSource) -> None:
        TypeChecker.check(value, 'ChatBoostSource')
        self._source = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'chat': self._chat,
            'boost_id': self._boost_id,
            'remove_date': self._remove_date,
            'source': self._source,
        }

class UserChatBoosts:
    """This object represents a list of boosts added to a chat by a user."""
    def __init__(self, **kwargs: Any):
        self._boosts = None
        if 'boosts' in kwargs:
            self.boosts = kwargs['boosts']

    @property
    def boosts(self) -> List[ChatBoost]:
        return self._boosts

    @boosts.setter
    def boosts(self, value: List[ChatBoost]) -> None:
        TypeChecker.check(value, 'List[ChatBoost]')
        self._boosts = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'boosts': self._boosts,
        }

class BusinessConnection:
    """Describes the connection of the bot with a business account."""
    def __init__(self, **kwargs: Any):
        self._id = None
        if 'id' in kwargs:
            self.id = kwargs['id']
        self._user = None
        if 'user' in kwargs:
            self.user = kwargs['user']
        self._user_chat_id = None
        if 'user_chat_id' in kwargs:
            self.user_chat_id = kwargs['user_chat_id']
        self._date = None
        if 'date' in kwargs:
            self.date = kwargs['date']
        self._can_reply = None
        if 'can_reply' in kwargs:
            self.can_reply = kwargs['can_reply']
        self._is_enabled = None
        if 'is_enabled' in kwargs:
            self.is_enabled = kwargs['is_enabled']

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._id = value

    @property
    def user(self) -> User:
        return self._user

    @user.setter
    def user(self, value: User) -> None:
        TypeChecker.check(value, 'User')
        self._user = value

    @property
    def user_chat_id(self) -> int:
        return self._user_chat_id

    @user_chat_id.setter
    def user_chat_id(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._user_chat_id = value

    @property
    def date(self) -> int:
        return self._date

    @date.setter
    def date(self, value: int) -> None:
        TypeChecker.check(value, 'int')
        self._date = value

    @property
    def can_reply(self) -> bool:
        return self._can_reply

    @can_reply.setter
    def can_reply(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._can_reply = value

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        TypeChecker.check(value, 'bool')
        self._is_enabled = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'user': self._user,
            'user_chat_id': self._user_chat_id,
            'date': self._date,
            'can_reply': self._can_reply,
            'is_enabled': self._is_enabled,
        }

class BusinessMessagesDeleted:
    """This object is received when messages are deleted from a connected business account."""
    def __init__(self, **kwargs: Any):
        self._business_connection_id = None
        if 'business_connection_id' in kwargs:
            self.business_connection_id = kwargs['business_connection_id']
        self._chat = None
        if 'chat' in kwargs:
            self.chat = kwargs['chat']
        self._message_ids = None
        if 'message_ids' in kwargs:
            self.message_ids = kwargs['message_ids']

    @property
    def business_connection_id(self) -> str:
        return self._business_connection_id

    @business_connection_id.setter
    def business_connection_id(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._business_connection_id = value

    @property
    def chat(self) -> Chat:
        return self._chat

    @chat.setter
    def chat(self, value: Chat) -> None:
        TypeChecker.check(value, 'Chat')
        self._chat = value

    @property
    def message_ids(self) -> List[int]:
        return self._message_ids

    @message_ids.setter
    def message_ids(self, value: List[int]) -> None:
        TypeChecker.check(value, 'List[int]')
        self._message_ids = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'business_connection_id': self._business_connection_id,
            'chat': self._chat,
            'message_ids': self._message_ids,
        }

class ResponseParameters:
    """Describes why a request was unsuccessful."""
    def __init__(self, **kwargs: Any):
        self._migrate_to_chat_id = None
        if 'migrate_to_chat_id' in kwargs:
            self.migrate_to_chat_id = kwargs['migrate_to_chat_id']
        self._retry_after = None
        if 'retry_after' in kwargs:
            self.retry_after = kwargs['retry_after']

    @property
    def migrate_to_chat_id(self) -> int | None:
        return self._migrate_to_chat_id

    @migrate_to_chat_id.setter
    def migrate_to_chat_id(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._migrate_to_chat_id = value

    @property
    def retry_after(self) -> int | None:
        return self._retry_after

    @retry_after.setter
    def retry_after(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._retry_after = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'migrate_to_chat_id': self._migrate_to_chat_id,
            'retry_after': self._retry_after,
        }

class InputMedia:
    """This object represents the content of a media message to be sent. It should be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class InputMediaPhoto:
    """Represents a photo to be sent."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']
        self._caption = None
        if 'caption' in kwargs:
            self.caption = kwargs['caption']
        self._parse_mode = None
        if 'parse_mode' in kwargs:
            self.parse_mode = kwargs['parse_mode']
        self._caption_entities = None
        if 'caption_entities' in kwargs:
            self.caption_entities = kwargs['caption_entities']
        self._show_caption_above_media = None
        if 'show_caption_above_media' in kwargs:
            self.show_caption_above_media = kwargs['show_caption_above_media']
        self._has_spoiler = None
        if 'has_spoiler' in kwargs:
            self.has_spoiler = kwargs['has_spoiler']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    @property
    def caption(self) -> str | None:
        return self._caption

    @caption.setter
    def caption(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._caption = value

    @property
    def parse_mode(self) -> str | None:
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._parse_mode = value

    @property
    def caption_entities(self) -> List[MessageEntity] | None:
        return self._caption_entities

    @caption_entities.setter
    def caption_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._caption_entities = value

    @property
    def show_caption_above_media(self) -> bool | None:
        return self._show_caption_above_media

    @show_caption_above_media.setter
    def show_caption_above_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._show_caption_above_media = value

    @property
    def has_spoiler(self) -> bool | None:
        return self._has_spoiler

    @has_spoiler.setter
    def has_spoiler(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_spoiler = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
            'caption': self._caption,
            'parse_mode': self._parse_mode,
            'caption_entities': self._caption_entities,
            'show_caption_above_media': self._show_caption_above_media,
            'has_spoiler': self._has_spoiler,
        }

class InputMediaVideo:
    """Represents a video to be sent."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._cover = None
        if 'cover' in kwargs:
            self.cover = kwargs['cover']
        self._start_timestamp = None
        if 'start_timestamp' in kwargs:
            self.start_timestamp = kwargs['start_timestamp']
        self._caption = None
        if 'caption' in kwargs:
            self.caption = kwargs['caption']
        self._parse_mode = None
        if 'parse_mode' in kwargs:
            self.parse_mode = kwargs['parse_mode']
        self._caption_entities = None
        if 'caption_entities' in kwargs:
            self.caption_entities = kwargs['caption_entities']
        self._show_caption_above_media = None
        if 'show_caption_above_media' in kwargs:
            self.show_caption_above_media = kwargs['show_caption_above_media']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._supports_streaming = None
        if 'supports_streaming' in kwargs:
            self.supports_streaming = kwargs['supports_streaming']
        self._has_spoiler = None
        if 'has_spoiler' in kwargs:
            self.has_spoiler = kwargs['has_spoiler']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    @property
    def thumbnail(self) -> str | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._thumbnail = value

    @property
    def cover(self) -> str | None:
        return self._cover

    @cover.setter
    def cover(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._cover = value

    @property
    def start_timestamp(self) -> int | None:
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._start_timestamp = value

    @property
    def caption(self) -> str | None:
        return self._caption

    @caption.setter
    def caption(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._caption = value

    @property
    def parse_mode(self) -> str | None:
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._parse_mode = value

    @property
    def caption_entities(self) -> List[MessageEntity] | None:
        return self._caption_entities

    @caption_entities.setter
    def caption_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._caption_entities = value

    @property
    def show_caption_above_media(self) -> bool | None:
        return self._show_caption_above_media

    @show_caption_above_media.setter
    def show_caption_above_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._show_caption_above_media = value

    @property
    def width(self) -> int | None:
        return self._width

    @width.setter
    def width(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._width = value

    @property
    def height(self) -> int | None:
        return self._height

    @height.setter
    def height(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._height = value

    @property
    def duration(self) -> int | None:
        return self._duration

    @duration.setter
    def duration(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._duration = value

    @property
    def supports_streaming(self) -> bool | None:
        return self._supports_streaming

    @supports_streaming.setter
    def supports_streaming(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._supports_streaming = value

    @property
    def has_spoiler(self) -> bool | None:
        return self._has_spoiler

    @has_spoiler.setter
    def has_spoiler(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_spoiler = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
            'thumbnail': self._thumbnail,
            'cover': self._cover,
            'start_timestamp': self._start_timestamp,
            'caption': self._caption,
            'parse_mode': self._parse_mode,
            'caption_entities': self._caption_entities,
            'show_caption_above_media': self._show_caption_above_media,
            'width': self._width,
            'height': self._height,
            'duration': self._duration,
            'supports_streaming': self._supports_streaming,
            'has_spoiler': self._has_spoiler,
        }

class InputMediaAnimation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._caption = None
        if 'caption' in kwargs:
            self.caption = kwargs['caption']
        self._parse_mode = None
        if 'parse_mode' in kwargs:
            self.parse_mode = kwargs['parse_mode']
        self._caption_entities = None
        if 'caption_entities' in kwargs:
            self.caption_entities = kwargs['caption_entities']
        self._show_caption_above_media = None
        if 'show_caption_above_media' in kwargs:
            self.show_caption_above_media = kwargs['show_caption_above_media']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._has_spoiler = None
        if 'has_spoiler' in kwargs:
            self.has_spoiler = kwargs['has_spoiler']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    @property
    def thumbnail(self) -> str | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._thumbnail = value

    @property
    def caption(self) -> str | None:
        return self._caption

    @caption.setter
    def caption(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._caption = value

    @property
    def parse_mode(self) -> str | None:
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._parse_mode = value

    @property
    def caption_entities(self) -> List[MessageEntity] | None:
        return self._caption_entities

    @caption_entities.setter
    def caption_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._caption_entities = value

    @property
    def show_caption_above_media(self) -> bool | None:
        return self._show_caption_above_media

    @show_caption_above_media.setter
    def show_caption_above_media(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._show_caption_above_media = value

    @property
    def width(self) -> int | None:
        return self._width

    @width.setter
    def width(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._width = value

    @property
    def height(self) -> int | None:
        return self._height

    @height.setter
    def height(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._height = value

    @property
    def duration(self) -> int | None:
        return self._duration

    @duration.setter
    def duration(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._duration = value

    @property
    def has_spoiler(self) -> bool | None:
        return self._has_spoiler

    @has_spoiler.setter
    def has_spoiler(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._has_spoiler = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
            'thumbnail': self._thumbnail,
            'caption': self._caption,
            'parse_mode': self._parse_mode,
            'caption_entities': self._caption_entities,
            'show_caption_above_media': self._show_caption_above_media,
            'width': self._width,
            'height': self._height,
            'duration': self._duration,
            'has_spoiler': self._has_spoiler,
        }

class InputMediaAudio:
    """Represents an audio file to be treated as music to be sent."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._caption = None
        if 'caption' in kwargs:
            self.caption = kwargs['caption']
        self._parse_mode = None
        if 'parse_mode' in kwargs:
            self.parse_mode = kwargs['parse_mode']
        self._caption_entities = None
        if 'caption_entities' in kwargs:
            self.caption_entities = kwargs['caption_entities']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._performer = None
        if 'performer' in kwargs:
            self.performer = kwargs['performer']
        self._title = None
        if 'title' in kwargs:
            self.title = kwargs['title']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    @property
    def thumbnail(self) -> str | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._thumbnail = value

    @property
    def caption(self) -> str | None:
        return self._caption

    @caption.setter
    def caption(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._caption = value

    @property
    def parse_mode(self) -> str | None:
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._parse_mode = value

    @property
    def caption_entities(self) -> List[MessageEntity] | None:
        return self._caption_entities

    @caption_entities.setter
    def caption_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._caption_entities = value

    @property
    def duration(self) -> int | None:
        return self._duration

    @duration.setter
    def duration(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._duration = value

    @property
    def performer(self) -> str | None:
        return self._performer

    @performer.setter
    def performer(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._performer = value

    @property
    def title(self) -> str | None:
        return self._title

    @title.setter
    def title(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._title = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
            'thumbnail': self._thumbnail,
            'caption': self._caption,
            'parse_mode': self._parse_mode,
            'caption_entities': self._caption_entities,
            'duration': self._duration,
            'performer': self._performer,
            'title': self._title,
        }

class InputMediaDocument:
    """Represents a general file to be sent."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._caption = None
        if 'caption' in kwargs:
            self.caption = kwargs['caption']
        self._parse_mode = None
        if 'parse_mode' in kwargs:
            self.parse_mode = kwargs['parse_mode']
        self._caption_entities = None
        if 'caption_entities' in kwargs:
            self.caption_entities = kwargs['caption_entities']
        self._disable_content_type_detection = None
        if 'disable_content_type_detection' in kwargs:
            self.disable_content_type_detection = kwargs['disable_content_type_detection']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    @property
    def thumbnail(self) -> str | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._thumbnail = value

    @property
    def caption(self) -> str | None:
        return self._caption

    @caption.setter
    def caption(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._caption = value

    @property
    def parse_mode(self) -> str | None:
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._parse_mode = value

    @property
    def caption_entities(self) -> List[MessageEntity] | None:
        return self._caption_entities

    @caption_entities.setter
    def caption_entities(self, value: List[MessageEntity] | None) -> None:
        TypeChecker.check(value, 'List[MessageEntity] | None')
        self._caption_entities = value

    @property
    def disable_content_type_detection(self) -> bool | None:
        return self._disable_content_type_detection

    @disable_content_type_detection.setter
    def disable_content_type_detection(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._disable_content_type_detection = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
            'thumbnail': self._thumbnail,
            'caption': self._caption,
            'parse_mode': self._parse_mode,
            'caption_entities': self._caption_entities,
            'disable_content_type_detection': self._disable_content_type_detection,
        }

class InputFile:
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser."""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class InputPaidMedia:
    """This object describes the paid media to be sent. Currently, it can be one of"""
    def __init__(self, **kwargs: Any):

    def to_dict(self) -> Dict[str, Any]:
        return {
        }

class InputPaidMediaPhoto:
    """The paid media to send is a photo."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
        }

class InputPaidMediaVideo:
    """The paid media to send is a video."""
    def __init__(self, **kwargs: Any):
        self._type = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        self._media = None
        if 'media' in kwargs:
            self.media = kwargs['media']
        self._thumbnail = None
        if 'thumbnail' in kwargs:
            self.thumbnail = kwargs['thumbnail']
        self._cover = None
        if 'cover' in kwargs:
            self.cover = kwargs['cover']
        self._start_timestamp = None
        if 'start_timestamp' in kwargs:
            self.start_timestamp = kwargs['start_timestamp']
        self._width = None
        if 'width' in kwargs:
            self.width = kwargs['width']
        self._height = None
        if 'height' in kwargs:
            self.height = kwargs['height']
        self._duration = None
        if 'duration' in kwargs:
            self.duration = kwargs['duration']
        self._supports_streaming = None
        if 'supports_streaming' in kwargs:
            self.supports_streaming = kwargs['supports_streaming']

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._type = value

    @property
    def media(self) -> str:
        return self._media

    @media.setter
    def media(self, value: str) -> None:
        TypeChecker.check(value, 'str')
        self._media = value

    @property
    def thumbnail(self) -> str | None:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._thumbnail = value

    @property
    def cover(self) -> str | None:
        return self._cover

    @cover.setter
    def cover(self, value: str | None) -> None:
        TypeChecker.check(value, 'str | None')
        self._cover = value

    @property
    def start_timestamp(self) -> int | None:
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._start_timestamp = value

    @property
    def width(self) -> int | None:
        return self._width

    @width.setter
    def width(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._width = value

    @property
    def height(self) -> int | None:
        return self._height

    @height.setter
    def height(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._height = value

    @property
    def duration(self) -> int | None:
        return self._duration

    @duration.setter
    def duration(self, value: int | None) -> None:
        TypeChecker.check(value, 'int | None')
        self._duration = value

    @property
    def supports_streaming(self) -> bool | None:
        return self._supports_streaming

    @supports_streaming.setter
    def supports_streaming(self, value: bool | None) -> None:
        TypeChecker.check(value, 'bool | None')
        self._supports_streaming = value

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self._type,
            'media': self._media,
            'thumbnail': self._thumbnail,
            'cover': self._cover,
            'start_timestamp': self._start_timestamp,
            'width': self._width,
            'height': self._height,
            'duration': self._duration,
            'supports_streaming': self._supports_streaming,
        }