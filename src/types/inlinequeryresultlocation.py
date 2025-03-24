from __future__ import annotations
from typing import Optional, List, Union

class InlineQueryResultLocation:
    def __init__(
        self,
        type: 'str',
        id: 'str',
        latitude: 'float',
        longitude: 'float',
        title: 'str',
        horizontal_accuracy: 'Optional[float]' = None,
        live_period: 'Optional[int]' = None,
        heading: 'Optional[int]' = None,
        proximity_alert_radius: 'Optional[int]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None,
        input_message_content: 'Optional[InputMessageContent]' = None,
        thumbnail_url: 'Optional[str]' = None,
        thumbnail_width: 'Optional[int]' = None,
        thumbnail_height: 'Optional[int]' = None
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