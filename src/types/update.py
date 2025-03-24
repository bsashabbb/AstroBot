from __future__ import annotations
from typing import Optional, List, Union

class Update:
    def __init__(
        self,
        update_id: 'int',
        message: 'Optional[Message]' = None,
        edited_message: 'Optional[Message]' = None,
        channel_post: 'Optional[Message]' = None,
        edited_channel_post: 'Optional[Message]' = None,
        business_connection: 'Optional[BusinessConnection]' = None,
        business_message: 'Optional[Message]' = None,
        edited_business_message: 'Optional[Message]' = None,
        deleted_business_messages: 'Optional[BusinessMessagesDeleted]' = None,
        message_reaction: 'Optional[MessageReactionUpdated]' = None,
        message_reaction_count: 'Optional[MessageReactionCountUpdated]' = None,
        inline_query: 'Optional[InlineQuery]' = None,
        chosen_inline_result: 'Optional[ChosenInlineResult]' = None,
        callback_query: 'Optional[CallbackQuery]' = None,
        shipping_query: 'Optional[ShippingQuery]' = None,
        pre_checkout_query: 'Optional[PreCheckoutQuery]' = None,
        purchased_paid_media: 'Optional[PaidMediaPurchased]' = None,
        poll: 'Optional[Poll]' = None,
        poll_answer: 'Optional[PollAnswer]' = None,
        my_chat_member: 'Optional[ChatMemberUpdated]' = None,
        chat_member: 'Optional[ChatMemberUpdated]' = None,
        chat_join_request: 'Optional[ChatJoinRequest]' = None,
        chat_boost: 'Optional[ChatBoostUpdated]' = None,
        removed_chat_boost: 'Optional[ChatBoostRemoved]' = None
    ):
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.business_connection = business_connection
        self.business_message = business_message
        self.edited_business_message = edited_business_message
        self.deleted_business_messages = deleted_business_messages
        self.message_reaction = message_reaction
        self.message_reaction_count = message_reaction_count
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.purchased_paid_media = purchased_paid_media
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request
        self.chat_boost = chat_boost
        self.removed_chat_boost = removed_chat_boost