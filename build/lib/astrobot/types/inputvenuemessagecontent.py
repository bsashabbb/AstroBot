from __future__ import annotations
from typing import Optional, List, Union, Any

class InputVenueMessageContent:
    """InputVenueMessageContent Telegram API type"""

    def __init__(
        self,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str],
        foursquare_type: Optional[str],
        google_place_id: Optional[str],
        google_place_type: Optional[str]
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
