from __future__ import annotations
from typing import Optional, List, Union

class getMyCommands:
    def __init__(
        self,
        scope: 'Optional[BotCommandScope]' = None,
        language_code: 'Optional[str]' = None
    ):
        self.scope = scope
        self.language_code = language_code