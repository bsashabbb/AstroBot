from typing import Optional, Dict, Any, Union, List

from .client import TelegramClient

from .models import *


class BotAPI(TelegramClient):

    async def get_me(self,

    ) -> Dict[str, Any]:
        """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object."""
        params = {

        }
        return await self._request(
            'getMe',
            {k: v for k, v in params.items() if v is not None}
        )

    async def log_out(self,

    ) -> Dict[str, Any]:
        """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
        params = {

        }
        return await self._request(
            'logOut',
            {k: v for k, v in params.items() if v is not None}
        )

    async def close(self,

    ) -> Dict[str, Any]:
        """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
        params = {

        }
        return await self._request(
            'close',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_message(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        text: str = None,
        parse_mode: str | None = None,
        entities: List[MessageEntity] | None = None,
        link_preview_options: LinkPreviewOptions | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send text messages. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'text': text,
            'parse_mode': parse_mode,
            'entities': entities,
            'link_preview_options': link_preview_options,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendMessage',
            {k: v for k, v in params.items() if v is not None}
        )

    async def forward_message(self,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        from_chat_id: int | str = None,
        video_start_timestamp: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        message_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent Message is returned."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'from_chat_id': from_chat_id,
            'video_start_timestamp': video_start_timestamp,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'message_id': message_id
        }
        return await self._request(
            'forwardMessage',
            {k: v for k, v in params.items() if v is not None}
        )

    async def forward_messages(self,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        from_chat_id: int | str = None,
        message_ids: List[int] = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages. On success, an array of MessageId of the sent messages is returned."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'from_chat_id': from_chat_id,
            'message_ids': message_ids,
            'disable_notification': disable_notification,
            'protect_content': protect_content
        }
        return await self._request(
            'forwardMessages',
            {k: v for k, v in params.items() if v is not None}
        )

    async def copy_message(self,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        from_chat_id: int | str = None,
        message_id: int = None,
        video_start_timestamp: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'video_start_timestamp': video_start_timestamp,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'copyMessage',
            {k: v for k, v in params.items() if v is not None}
        )

    async def copy_messages(self,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        from_chat_id: int | str = None,
        message_ids: List[int] = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        remove_caption: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz poll can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method forwardMessages, but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an array of MessageId of the sent messages is returned."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'from_chat_id': from_chat_id,
            'message_ids': message_ids,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'remove_caption': remove_caption
        }
        return await self._request(
            'copyMessages',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_photo(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        photo: InputFile | str = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send photos. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'photo': photo,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendPhoto',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_audio(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        audio: InputFile | str = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        duration: int | None = None,
        performer: str | None = None,
        title: str | None = None,
        thumbnail: InputFile | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future. For sending voice messages, use the sendVoice method instead."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'audio': audio,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'duration': duration,
            'performer': performer,
            'title': title,
            'thumbnail': thumbnail,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendAudio',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_document(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        document: InputFile | str = None,
        thumbnail: InputFile | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        disable_content_type_detection: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'document': document,
            'thumbnail': thumbnail,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'disable_content_type_detection': disable_content_type_detection,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendDocument',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_video(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        video: InputFile | str = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: InputFile | str | None = None,
        cover: InputFile | str | None = None,
        start_timestamp: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        supports_streaming: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'video': video,
            'duration': duration,
            'width': width,
            'height': height,
            'thumbnail': thumbnail,
            'cover': cover,
            'start_timestamp': start_timestamp,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'supports_streaming': supports_streaming,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendVideo',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_animation(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        animation: InputFile | str = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: InputFile | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'animation': animation,
            'duration': duration,
            'width': width,
            'height': height,
            'thumbnail': thumbnail,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendAnimation',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_voice(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        voice: InputFile | str = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS, or in .MP3 format, or in .M4A format (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'voice': voice,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'duration': duration,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendVoice',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_video_note(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        video_note: InputFile | str = None,
        duration: int | None = None,
        length: int | None = None,
        thumbnail: InputFile | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """As of v.4.0, Telegram clients support rounded square MPEG4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'video_note': video_note,
            'duration': duration,
            'length': length,
            'thumbnail': thumbnail,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendVideoNote',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_paid_media(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        star_count: int = None,
        media: List[InputPaidMedia] = None,
        payload: str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: List[MessageEntity] | None = None,
        show_caption_above_media: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send paid media. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'star_count': star_count,
            'media': media,
            'payload': payload,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'show_caption_above_media': show_caption_above_media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendPaidMedia',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_media_group(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        media: List[InputMediaAudio | InputMediaDocument | InputMediaPhoto and InputMediaVideo] = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None
    ) -> Dict[str, Any]:
        """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'media': media,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters
        }
        return await self._request(
            'sendMediaGroup',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_location(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        latitude: float = None,
        longitude: float = None,
        horizontal_accuracy: float | None = None,
        live_period: int | None = None,
        heading: int | None = None,
        proximity_alert_radius: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send point on the map. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'latitude': latitude,
            'longitude': longitude,
            'horizontal_accuracy': horizontal_accuracy,
            'live_period': live_period,
            'heading': heading,
            'proximity_alert_radius': proximity_alert_radius,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendLocation',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_venue(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        latitude: float = None,
        longitude: float = None,
        title: str = None,
        address: str = None,
        foursquare_id: str | None = None,
        foursquare_type: str | None = None,
        google_place_id: str | None = None,
        google_place_type: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send information about a venue. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address,
            'foursquare_id': foursquare_id,
            'foursquare_type': foursquare_type,
            'google_place_id': google_place_id,
            'google_place_type': google_place_type,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendVenue',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_contact(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        phone_number: str = None,
        first_name: str = None,
        last_name: str | None = None,
        vcard: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send phone contacts. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'last_name': last_name,
            'vcard': vcard,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendContact',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_poll(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        question: str = None,
        question_parse_mode: str | None = None,
        question_entities: List[MessageEntity] | None = None,
        options: List[InputPollOption] = None,
        is_anonymous: bool | None = None,
        type: str | None = None,
        allows_multiple_answers: bool | None = None,
        correct_option_id: int | None = None,
        explanation: str | None = None,
        explanation_parse_mode: str | None = None,
        explanation_entities: List[MessageEntity] | None = None,
        open_period: int | None = None,
        close_date: int | None = None,
        is_closed: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send a native poll. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'question': question,
            'question_parse_mode': question_parse_mode,
            'question_entities': question_entities,
            'options': options,
            'is_anonymous': is_anonymous,
            'type': type,
            'allows_multiple_answers': allows_multiple_answers,
            'correct_option_id': correct_option_id,
            'explanation': explanation,
            'explanation_parse_mode': explanation_parse_mode,
            'explanation_entities': explanation_entities,
            'open_period': open_period,
            'close_date': close_date,
            'is_closed': is_closed,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendPoll',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_dice(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_parameters: ReplyParameters | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply | None = None
    ) -> Dict[str, Any]:
        """Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'emoji': emoji,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'allow_paid_broadcast': allow_paid_broadcast,
            'message_effect_id': message_effect_id,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup
        }
        return await self._request(
            'sendDice',
            {k: v for k, v in params.items() if v is not None}
        )

    async def send_chat_action(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_thread_id: int | None = None,
        action: str = None
    ) -> Dict[str, Any]:
        """Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success. We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'action': action
        }
        return await self._request(
            'sendChatAction',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_message_reaction(self,
        chat_id: int | str = None,
        message_id: int = None,
        reaction: List[ReactionType] | None = None,
        is_big: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the chosen reactions on a message. Service messages of some types can't be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can't use paid reactions. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'reaction': reaction,
            'is_big': is_big
        }
        return await self._request(
            'setMessageReaction',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_user_profile_photos(self,
        user_id: int = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> Dict[str, Any]:
        """Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object."""
        params = {
            'user_id': user_id,
            'offset': offset,
            'limit': limit
        }
        return await self._request(
            'getUserProfilePhotos',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_user_emoji_status(self,
        user_id: int = None,
        emoji_status_custom_emoji_id: str | None = None,
        emoji_status_expiration_date: int | None = None
    ) -> Dict[str, Any]:
        """Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess. Returns True on success."""
        params = {
            'user_id': user_id,
            'emoji_status_custom_emoji_id': emoji_status_custom_emoji_id,
            'emoji_status_expiration_date': emoji_status_expiration_date
        }
        return await self._request(
            'setUserEmojiStatus',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_file(self,
        file_id: str = None
    ) -> Dict[str, Any]:
        """Use this method to get basic information about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again."""
        params = {
            'file_id': file_id
        }
        return await self._request(
            'getFile',
            {k: v for k, v in params.items() if v is not None}
        )

    async def ban_chat_member(self,
        chat_id: int | str = None,
        user_id: int = None,
        until_date: int | None = None,
        revoke_messages: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'until_date': until_date,
            'revoke_messages': revoke_messages
        }
        return await self._request(
            'banChatMember',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unban_chat_member(self,
        chat_id: int | str = None,
        user_id: int = None,
        only_if_banned: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'only_if_banned': only_if_banned
        }
        return await self._request(
            'unbanChatMember',
            {k: v for k, v in params.items() if v is not None}
        )

    async def restrict_chat_member(self,
        chat_id: int | str = None,
        user_id: int = None,
        permissions: ChatPermissions = None,
        use_independent_chat_permissions: bool | None = None,
        until_date: int | None = None
    ) -> Dict[str, Any]:
        """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions': permissions,
            'use_independent_chat_permissions': use_independent_chat_permissions,
            'until_date': until_date
        }
        return await self._request(
            'restrictChatMember',
            {k: v for k, v in params.items() if v is not None}
        )

    async def promote_chat_member(self,
        chat_id: int | str = None,
        user_id: int = None,
        is_anonymous: bool | None = None,
        can_manage_chat: bool | None = None,
        can_delete_messages: bool | None = None,
        can_manage_video_chats: bool | None = None,
        can_restrict_members: bool | None = None,
        can_promote_members: bool | None = None,
        can_change_info: bool | None = None,
        can_invite_users: bool | None = None,
        can_post_stories: bool | None = None,
        can_edit_stories: bool | None = None,
        can_delete_stories: bool | None = None,
        can_post_messages: bool | None = None,
        can_edit_messages: bool | None = None,
        can_pin_messages: bool | None = None,
        can_manage_topics: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'is_anonymous': is_anonymous,
            'can_manage_chat': can_manage_chat,
            'can_delete_messages': can_delete_messages,
            'can_manage_video_chats': can_manage_video_chats,
            'can_restrict_members': can_restrict_members,
            'can_promote_members': can_promote_members,
            'can_change_info': can_change_info,
            'can_invite_users': can_invite_users,
            'can_post_stories': can_post_stories,
            'can_edit_stories': can_edit_stories,
            'can_delete_stories': can_delete_stories,
            'can_post_messages': can_post_messages,
            'can_edit_messages': can_edit_messages,
            'can_pin_messages': can_pin_messages,
            'can_manage_topics': can_manage_topics
        }
        return await self._request(
            'promoteChatMember',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_administrator_custom_title(self,
        chat_id: int | str = None,
        user_id: int = None,
        custom_title: str = None
    ) -> Dict[str, Any]:
        """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title': custom_title
        }
        return await self._request(
            'setChatAdministratorCustomTitle',
            {k: v for k, v in params.items() if v is not None}
        )

    async def ban_chat_sender_chat(self,
        chat_id: int | str = None,
        sender_chat_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id
        }
        return await self._request(
            'banChatSenderChat',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unban_chat_sender_chat(self,
        chat_id: int | str = None,
        sender_chat_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id
        }
        return await self._request(
            'unbanChatSenderChat',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_permissions(self,
        chat_id: int | str = None,
        permissions: ChatPermissions = None,
        use_independent_chat_permissions: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'permissions': permissions,
            'use_independent_chat_permissions': use_independent_chat_permissions
        }
        return await self._request(
            'setChatPermissions',
            {k: v for k, v in params.items() if v is not None}
        )

    async def export_chat_invite_link(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'exportChatInviteLink',
            {k: v for k, v in params.items() if v is not None}
        )

    async def create_chat_invite_link(self,
        chat_id: int | str = None,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object."""
        params = {
            'chat_id': chat_id,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request
        }
        return await self._request(
            'createChatInviteLink',
            {k: v for k, v in params.items() if v is not None}
        )

    async def edit_chat_invite_link(self,
        chat_id: int | str = None,
        invite_link: str = None,
        name: str | None = None,
        expire_date: int | None = None,
        member_limit: int | None = None,
        creates_join_request: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object."""
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request
        }
        return await self._request(
            'editChatInviteLink',
            {k: v for k, v in params.items() if v is not None}
        )

    async def create_chat_subscription_invite_link(self,
        chat_id: int | str = None,
        name: str | None = None,
        subscription_period: int = None,
        subscription_price: int = None
    ) -> Dict[str, Any]:
        """Use this method to create a subscription invite link for a channel chat. The bot must have the can_invite_users administrator rights. The link can be edited using the method editChatSubscriptionInviteLink or revoked using the method revokeChatInviteLink. Returns the new invite link as a ChatInviteLink object."""
        params = {
            'chat_id': chat_id,
            'name': name,
            'subscription_period': subscription_period,
            'subscription_price': subscription_price
        }
        return await self._request(
            'createChatSubscriptionInviteLink',
            {k: v for k, v in params.items() if v is not None}
        )

    async def edit_chat_subscription_invite_link(self,
        chat_id: int | str = None,
        invite_link: str = None,
        name: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to edit a subscription invite link created by the bot. The bot must have the can_invite_users administrator rights. Returns the edited invite link as a ChatInviteLink object."""
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            'name': name
        }
        return await self._request(
            'editChatSubscriptionInviteLink',
            {k: v for k, v in params.items() if v is not None}
        )

    async def revoke_chat_invite_link(self,
        chat_id: int | str = None,
        invite_link: str = None
    ) -> Dict[str, Any]:
        """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object."""
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link
        }
        return await self._request(
            'revokeChatInviteLink',
            {k: v for k, v in params.items() if v is not None}
        )

    async def approve_chat_join_request(self,
        chat_id: int | str = None,
        user_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await self._request(
            'approveChatJoinRequest',
            {k: v for k, v in params.items() if v is not None}
        )

    async def decline_chat_join_request(self,
        chat_id: int | str = None,
        user_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await self._request(
            'declineChatJoinRequest',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_photo(self,
        chat_id: int | str = None,
        photo: InputFile = None
    ) -> Dict[str, Any]:
        """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'photo': photo
        }
        return await self._request(
            'setChatPhoto',
            {k: v for k, v in params.items() if v is not None}
        )

    async def delete_chat_photo(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'deleteChatPhoto',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_title(self,
        chat_id: int | str = None,
        title: str = None
    ) -> Dict[str, Any]:
        """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'title': title
        }
        return await self._request(
            'setChatTitle',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_description(self,
        chat_id: int | str = None,
        description: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'description': description
        }
        return await self._request(
            'setChatDescription',
            {k: v for k, v in params.items() if v is not None}
        )

    async def pin_chat_message(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_id: int = None,
        disable_notification: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id,
            'disable_notification': disable_notification
        }
        return await self._request(
            'pinChatMessage',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unpin_chat_message(self,
        business_connection_id: str | None = None,
        chat_id: int | str = None,
        message_id: int | None = None
    ) -> Dict[str, Any]:
        """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
        params = {
            'business_connection_id': business_connection_id,
            'chat_id': chat_id,
            'message_id': message_id
        }
        return await self._request(
            'unpinChatMessage',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unpin_all_chat_messages(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'unpinAllChatMessages',
            {k: v for k, v in params.items() if v is not None}
        )

    async def leave_chat(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method for your bot to leave a group, supergroup or channel. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'leaveChat',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_chat(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to get up-to-date information about the chat. Returns a ChatFullInfo object on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'getChat',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_chat_administrators(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to get a list of administrators in a chat, which aren't bots. Returns an Array of ChatMember objects."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'getChatAdministrators',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_chat_member_count(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to get the number of members in a chat. Returns Int on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'getChatMemberCount',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_chat_member(self,
        chat_id: int | str = None,
        user_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat. Returns a ChatMember object on success."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await self._request(
            'getChatMember',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_sticker_set(self,
        chat_id: int | str = None,
        sticker_set_name: str = None
    ) -> Dict[str, Any]:
        """Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name
        }
        return await self._request(
            'setChatStickerSet',
            {k: v for k, v in params.items() if v is not None}
        )

    async def delete_chat_sticker_set(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'deleteChatStickerSet',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_forum_topic_icon_stickers(self,

    ) -> Dict[str, Any]:
        """Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters. Returns an Array of Sticker objects."""
        params = {

        }
        return await self._request(
            'getForumTopicIconStickers',
            {k: v for k, v in params.items() if v is not None}
        )

    async def create_forum_topic(self,
        chat_id: int | str = None,
        name: str = None,
        icon_color: int | None = None,
        icon_custom_emoji_id: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to create a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns information about the created topic as a ForumTopic object."""
        params = {
            'chat_id': chat_id,
            'name': name,
            'icon_color': icon_color,
            'icon_custom_emoji_id': icon_custom_emoji_id
        }
        return await self._request(
            'createForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def edit_forum_topic(self,
        chat_id: int | str = None,
        message_thread_id: int = None,
        name: str | None = None,
        icon_custom_emoji_id: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'name': name,
            'icon_custom_emoji_id': icon_custom_emoji_id
        }
        return await self._request(
            'editForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def close_forum_topic(self,
        chat_id: int | str = None,
        message_thread_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await self._request(
            'closeForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def reopen_forum_topic(self,
        chat_id: int | str = None,
        message_thread_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await self._request(
            'reopenForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def delete_forum_topic(self,
        chat_id: int | str = None,
        message_thread_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to delete a forum topic along with all its messages in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_delete_messages administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await self._request(
            'deleteForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unpin_all_forum_topic_messages(self,
        chat_id: int | str = None,
        message_thread_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id
        }
        return await self._request(
            'unpinAllForumTopicMessages',
            {k: v for k, v in params.items() if v is not None}
        )

    async def edit_general_forum_topic(self,
        chat_id: int | str = None,
        name: str = None
    ) -> Dict[str, Any]:
        """Use this method to edit the name of the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'name': name
        }
        return await self._request(
            'editGeneralForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def close_general_forum_topic(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to close an open 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'closeGeneralForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def reopen_general_forum_topic(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to reopen a closed 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically unhidden if it was hidden. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'reopenGeneralForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def hide_general_forum_topic(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to hide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. The topic will be automatically closed if it was open. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'hideGeneralForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unhide_general_forum_topic(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to unhide the 'General' topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'unhideGeneralForumTopic',
            {k: v for k, v in params.items() if v is not None}
        )

    async def unpin_all_general_forum_topic_messages(self,
        chat_id: int | str = None
    ) -> Dict[str, Any]:
        """Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have the can_pin_messages administrator right in the supergroup. Returns True on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'unpinAllGeneralForumTopicMessages',
            {k: v for k, v in params.items() if v is not None}
        )

    async def answer_callback_query(self,
        callback_query_id: str = None,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None
    ) -> Dict[str, Any]:
        """Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned."""
        params = {
            'callback_query_id': callback_query_id,
            'text': text,
            'show_alert': show_alert,
            'url': url,
            'cache_time': cache_time
        }
        return await self._request(
            'answerCallbackQuery',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_user_chat_boosts(self,
        chat_id: int | str = None,
        user_id: int = None
    ) -> Dict[str, Any]:
        """Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat. Returns a UserChatBoosts object."""
        params = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        return await self._request(
            'getUserChatBoosts',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_business_connection(self,
        business_connection_id: str = None
    ) -> Dict[str, Any]:
        """Use this method to get information about the connection of the bot with a business account. Returns a BusinessConnection object on success."""
        params = {
            'business_connection_id': business_connection_id
        }
        return await self._request(
            'getBusinessConnection',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_my_commands(self,
        commands: List[BotCommand] = None,
        scope: BotCommandScope | None = None,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the list of the bot's commands. See this manual for more details about bot commands. Returns True on success."""
        params = {
            'commands': commands,
            'scope': scope,
            'language_code': language_code
        }
        return await self._request(
            'setMyCommands',
            {k: v for k, v in params.items() if v is not None}
        )

    async def delete_my_commands(self,
        scope: BotCommandScope | None = None,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success."""
        params = {
            'scope': scope,
            'language_code': language_code
        }
        return await self._request(
            'deleteMyCommands',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_my_commands(self,
        scope: BotCommandScope | None = None,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to get the current list of the bot's commands for the given scope and user language. Returns an Array of BotCommand objects. If commands aren't set, an empty list is returned."""
        params = {
            'scope': scope,
            'language_code': language_code
        }
        return await self._request(
            'getMyCommands',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_my_name(self,
        name: str | None = None,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the bot's name. Returns True on success."""
        params = {
            'name': name,
            'language_code': language_code
        }
        return await self._request(
            'setMyName',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_my_name(self,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to get the current bot name for the given user language. Returns BotName on success."""
        params = {
            'language_code': language_code
        }
        return await self._request(
            'getMyName',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_my_description(self,
        description: str | None = None,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty. Returns True on success."""
        params = {
            'description': description,
            'language_code': language_code
        }
        return await self._request(
            'setMyDescription',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_my_description(self,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to get the current bot description for the given user language. Returns BotDescription on success."""
        params = {
            'language_code': language_code
        }
        return await self._request(
            'getMyDescription',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_my_short_description(self,
        short_description: str | None = None,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot. Returns True on success."""
        params = {
            'short_description': short_description,
            'language_code': language_code
        }
        return await self._request(
            'setMyShortDescription',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_my_short_description(self,
        language_code: str | None = None
    ) -> Dict[str, Any]:
        """Use this method to get the current bot short description for the given user language. Returns BotShortDescription on success."""
        params = {
            'language_code': language_code
        }
        return await self._request(
            'getMyShortDescription',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_chat_menu_button(self,
        chat_id: int | None = None,
        menu_button: MenuButton | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns True on success."""
        params = {
            'chat_id': chat_id,
            'menu_button': menu_button
        }
        return await self._request(
            'setChatMenuButton',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_chat_menu_button(self,
        chat_id: int | None = None
    ) -> Dict[str, Any]:
        """Use this method to get the current value of the bot's menu button in a private chat, or the default menu button. Returns MenuButton on success."""
        params = {
            'chat_id': chat_id
        }
        return await self._request(
            'getChatMenuButton',
            {k: v for k, v in params.items() if v is not None}
        )

    async def set_my_default_administrator_rights(self,
        rights: ChatAdministratorRights | None = None,
        for_channels: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot. Returns True on success."""
        params = {
            'rights': rights,
            'for_channels': for_channels
        }
        return await self._request(
            'setMyDefaultAdministratorRights',
            {k: v for k, v in params.items() if v is not None}
        )

    async def get_my_default_administrator_rights(self,
        for_channels: bool | None = None
    ) -> Dict[str, Any]:
        """Use this method to get the current default administrator rights of the bot. Returns ChatAdministratorRights on success."""
        params = {
            'for_channels': for_channels
        }
        return await self._request(
            'getMyDefaultAdministratorRights',
            {k: v for k, v in params.items() if v is not None}
        )