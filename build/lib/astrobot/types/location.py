from __future__ import annotations
from typing import Optional, List, Union, Any

class Location:
    """Location Telegram API type"""

    def __init__(
        self,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float],
        live_period: Optional[int],
        heading: Optional[int],
        proximity_alert_radius: Optional[int]
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
