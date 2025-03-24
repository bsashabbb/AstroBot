from __future__ import annotations
from typing import Optional, List, Union

class ShippingAddress:
    def __init__(
        self,
        country_code: 'str',
        state: 'str',
        city: 'str',
        street_line1: 'str',
        street_line2: 'str',
        post_code: 'str'
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code