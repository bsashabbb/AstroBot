from __future__ import annotations
from typing import Optional, List, Union

class revokeChatInviteLink:
    def __init__(
        self,
        chat_id: 'Union[str]',
        invite_link: 'str'
    ):
        self.chat_id = chat_id
        self.invite_link = invite_link