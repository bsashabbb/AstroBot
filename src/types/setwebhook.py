from __future__ import annotations
from typing import Optional, List, Union

class setWebhook:
    def __init__(
        self,
        url: 'str',
        certificate: 'Optional[InputFile]' = None,
        ip_address: 'Optional[str]' = None,
        max_connections: 'Optional[int]' = None,
        allowed_updates: 'Optional[List[str]]' = None,
        drop_pending_updates: 'Optional[bool]' = None,
        secret_token: 'Optional[str]' = None
    ):
        self.url = url
        self.certificate = certificate
        self.ip_address = ip_address
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates
        self.drop_pending_updates = drop_pending_updates
        self.secret_token = secret_token