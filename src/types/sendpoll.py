from __future__ import annotations
from typing import Optional, List, Union

class sendPoll:
    def __init__(
        self,
        chat_id: 'Union[str]',
        question: 'str',
        options: 'List[InputPollOption]',
        business_connection_id: 'Optional[str]' = None,
        message_thread_id: 'Optional[int]' = None,
        question_parse_mode: 'Optional[str]' = None,
        question_entities: 'Optional[List[MessageEntity]]' = None,
        is_anonymous: 'Optional[bool]' = None,
        type: 'Optional[str]' = None,
        allows_multiple_answers: 'Optional[bool]' = None,
        correct_option_id: 'Optional[int]' = None,
        explanation: 'Optional[str]' = None,
        explanation_parse_mode: 'Optional[str]' = None,
        explanation_entities: 'Optional[List[MessageEntity]]' = None,
        open_period: 'Optional[int]' = None,
        close_date: 'Optional[int]' = None,
        is_closed: 'Optional[bool]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        allow_paid_broadcast: 'Optional[bool]' = None,
        message_effect_id: 'Optional[str]' = None,
        reply_parameters: 'Optional[ReplyParameters]' = None,
        reply_markup: 'Optional[Union[ReplyKeyboardMarkup]]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.question = question
        self.question_parse_mode = question_parse_mode
        self.question_entities = question_entities
        self.options = options
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_parse_mode = explanation_parse_mode
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
        self.is_closed = is_closed
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.allow_paid_broadcast = allow_paid_broadcast
        self.message_effect_id = message_effect_id
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup