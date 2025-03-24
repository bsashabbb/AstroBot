from __future__ import annotations
from typing import Optional, List, Union

class Venue:
    def __init__(
        self,
        location: 'Location',
        title: 'str',
        address: 'str',
        foursquare_id: 'Optional[str]' = None,
        foursquare_type: 'Optional[str]' = None,
        google_place_id: 'Optional[str]' = None,
        google_place_type: 'Optional[str]' = None
    ):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type