from __future__ import annotations
from typing import Optional, List, Union

class InputVenueMessageContent:
    def __init__(
        self,
        latitude: 'float',
        longitude: 'float',
        title: 'str',
        address: 'str',
        foursquare_id: 'Optional[str]' = None,
        foursquare_type: 'Optional[str]' = None,
        google_place_id: 'Optional[str]' = None,
        google_place_type: 'Optional[str]' = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type