from __future__ import annotations
from typing import Optional, List, Union

class editMessageLiveLocation:
    def __init__(
        self,
        latitude: 'float',
        longitude: 'float',
        business_connection_id: 'Optional[str]' = None,
        chat_id: 'Optional[Union[str]]' = None,
        message_id: 'Optional[int]' = None,
        inline_message_id: 'Optional[str]' = None,
        live_period: 'Optional[int]' = None,
        horizontal_accuracy: 'Optional[float]' = None,
        heading: 'Optional[int]' = None,
        proximity_alert_radius: 'Optional[int]' = None,
        reply_markup: 'Optional[InlineKeyboardMarkup]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.latitude = latitude
        self.longitude = longitude
        self.live_period = live_period
        self.horizontal_accuracy = horizontal_accuracy
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup