from __future__ import annotations
from typing import Optional, List, Union, Any

class InlineQueryResultVenue:
    """InlineQueryResultVenue Telegram API type"""

    def __init__(
        self,
        type: str,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str],
        foursquare_type: Optional[str],
        google_place_id: Optional[str],
        google_place_type: Optional[str],
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
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height
