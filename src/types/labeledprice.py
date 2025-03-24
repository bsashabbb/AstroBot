from __future__ import annotations
from typing import Optional, List, Union

class LabeledPrice:
    def __init__(
        self,
        label: 'str',
        amount: 'int'
    ):
        self.label = label
        self.amount = amount