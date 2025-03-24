from __future__ import annotations
from typing import Optional, List, Union

class setMyDefaultAdministratorRights:
    def __init__(
        self,
        rights: 'Optional[ChatAdministratorRights]' = None,
        for_channels: 'Optional[bool]' = None
    ):
        self.rights = rights
        self.for_channels = for_channels