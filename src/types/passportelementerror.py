from __future__ import annotations
from typing import Optional, List, Union

class PassportElementError:
    def __init__(
        self,
        source: 'str',
        type: 'str',
        field_name: 'str',
        data_hash: 'str',
        message: 'str'
    ):
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message