from __future__ import annotations
from typing import Optional, List, Union

class ProximityAlertTriggered:
    def __init__(
        self,
        traveler: 'User',
        watcher: 'User',
        distance: 'int'
    ):
        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance