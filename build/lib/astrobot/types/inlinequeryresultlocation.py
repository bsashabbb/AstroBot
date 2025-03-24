from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultLocation:
    """InlineQueryResultLocation Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        horizontal_accuracy: Optional[float],
        live_period: Optional[int],
        heading: Optional[int],
        proximity_alert_radius: Optional[int],
        reply_markup: Optional['InlineKeyboardMarkup'],
        input_message_content: Optional['InputMessageContent'],
        thumbnail_url: Optional[str],
        thumbnail_width: Optional[int],
        thumbnail_height: Optional[int]
    ):
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
