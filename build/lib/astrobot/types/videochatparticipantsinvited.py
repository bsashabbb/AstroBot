from __future__ import annotations
from typing import Optional, List, Union, Any

class VideoChatParticipantsInvited:
    """VideoChatParticipantsInvited Telegram API type"""

    def __init__(
        self,
        users: List['User']
    ):
        self.users = users
