from __future__ import annotations
from typing import Optional, List, Union

class WebhookInfo:
    def __init__(
        self,
        has_custom_certificate: 'bool',
        pending_update_count: 'int',
        url: 'Optional[str]' = None,
        ip_address: 'Optional[str]' = None,
        last_error_date: 'Optional[int]' = None,
        last_error_message: 'Optional[str]' = None,
        last_synchronization_error_date: 'Optional[int]' = None,
        max_connections: 'Optional[int]' = None,
        allowed_updates: 'Optional[List[str]]' = None
    ):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates