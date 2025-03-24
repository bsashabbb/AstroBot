from __future__ import annotations
from typing import Optional, List, Union

class InputLocationMessageContent:
    def __init__(
        self,
        latitude: 'float',
        longitude: 'float',
        horizontal_accuracy: 'Optional[float]' = None,
        live_period: 'Optional[int]' = None,
        heading: 'Optional[int]' = None,
        proximity_alert_radius: 'Optional[int]' = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius