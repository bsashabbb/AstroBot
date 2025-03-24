from __future__ import annotations
from typing import Optional, List, Union

class sendLocation:
    def __init__(
        self,
        chat_id: 'Union[str]',
        latitude: 'float',
        longitude: 'float',
        business_connection_id: 'Optional[str]' = None,
        message_thread_id: 'Optional[int]' = None,
        horizontal_accuracy: 'Optional[float]' = None,
        live_period: 'Optional[int]' = None,
        heading: 'Optional[int]' = None,
        proximity_alert_radius: 'Optional[int]' = None,
        disable_notification: 'Optional[bool]' = None,
        protect_content: 'Optional[bool]' = None,
        allow_paid_broadcast: 'Optional[bool]' = None,
        message_effect_id: 'Optional[str]' = None,
        reply_parameters: 'Optional[ReplyParameters]' = None,
        reply_markup: 'Optional[Union[ReplyKeyboardMarkup]]' = None
    ):
        self.business_connection_id = business_connection_id
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.allow_paid_broadcast = allow_paid_broadcast
        self.message_effect_id = message_effect_id
        self.reply_parameters = reply_parameters
        self.reply_markup = reply_markup