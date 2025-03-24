from __future__ import annotations
from typing import Optional, List, Union

class setMyCommands:
    def __init__(
        self,
        commands: 'List[BotCommand]',
        scope: 'Optional[BotCommandScope]' = None,
        language_code: 'Optional[str]' = None
    ):
        self.commands = commands
        self.scope = scope
        self.language_code = language_code