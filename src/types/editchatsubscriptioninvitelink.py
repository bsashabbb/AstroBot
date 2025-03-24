from __future__ import annotations
from typing import Optional, List, Union

class editChatSubscriptionInviteLink:
    def __init__(
        self,
        chat_id: 'Union[str]',
        invite_link: 'str',
        name: 'Optional[str]' = None
    ):
        self.chat_id = chat_id
        self.invite_link = invite_link
        self.name = name