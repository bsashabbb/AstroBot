from __future__ import annotations
from typing import Optional, List, Union, Any
from . import BusinessConnection, BusinessMessagesDeleted, CallbackQuery, ChatBoostRemoved, ChatBoostUpdated, ChatJoinRequest, ChatMemberUpdated, ChosenInlineResult, InlineQuery, Message, MessageReactionCountUpdated, MessageReactionUpdated, PaidMediaPurchased, Poll, PollAnswer, PreCheckoutQuery, ShippingQuery

class Update:
    def __init__(
        self,
        update_id: int,
        message: Optional['Message'],
        edited_message: Optional['Message'],
        channel_post: Optional['Message'],
        edited_channel_post: Optional['Message'],
        business_connection: Optional['BusinessConnection'],
        business_message: Optional['Message'],
        edited_business_message: Optional['Message'],
        deleted_business_messages: Optional['BusinessMessagesDeleted'],
        message_reaction: Optional['MessageReactionUpdated'],
        message_reaction_count: Optional['MessageReactionCountUpdated'],
        inline_query: Optional['InlineQuery'],
        chosen_inline_result: Optional['ChosenInlineResult'],
        callback_query: Optional['CallbackQuery'],
        shipping_query: Optional['ShippingQuery'],
        pre_checkout_query: Optional['PreCheckoutQuery'],
        purchased_paid_media: Optional['PaidMediaPurchased'],
        poll: Optional['Poll'],
        poll_answer: Optional['PollAnswer'],
        my_chat_member: Optional['ChatMemberUpdated'],
        chat_member: Optional['ChatMemberUpdated'],
        chat_join_request: Optional['ChatJoinRequest'],
        chat_boost: Optional['ChatBoostUpdated'],
        removed_chat_boost: Optional['ChatBoostRemoved']
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
