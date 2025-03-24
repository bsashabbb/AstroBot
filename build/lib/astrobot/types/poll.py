from __future__ import annotations
from typing import Optional, List, Union, Any

class Poll:
    """Poll Telegram API type"""

    def __init__(
        self,
        id: str,
        question: str,
        question_entities: Optional[List['MessageEntity']],
        options: List['PollOption'],
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool,
        type: str,
        allows_multiple_answers: bool,
        correct_option_id: Optional[int],
        explanation: Optional[str],
        explanation_entities: Optional[List['MessageEntity']],
        open_period: Optional[int],
        close_date: Optional[int]
    ):
        self.id = id
        self.question = question
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
