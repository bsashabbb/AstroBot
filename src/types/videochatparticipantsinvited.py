from __future__ import annotations
from typing import Optional, List, Union

class VideoChatParticipantsInvited:
    def __init__(
        self,
        users: 'List[User]'
    ):
        self.users = users