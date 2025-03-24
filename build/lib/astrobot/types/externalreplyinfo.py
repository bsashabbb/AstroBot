from __future__ import annotations
from typing import Optional, List, Union, Any

class ExternalReplyInfo:
    """ExternalReplyInfo Telegram API type"""

    def __init__(
        self,
        origin: 'MessageOrigin',
        chat: Optional['Chat'],
        message_id: Optional[int],
        link_preview_options: Optional['LinkPreviewOptions'],
        animation: Optional['Animation'],
        audio: Optional['Audio'],
        document: Optional['Document'],
        paid_media: Optional['PaidMediaInfo'],
        photo: Optional[List['PhotoSize']],
        sticker: Optional['Sticker'],
        story: Optional['Story'],
        video: Optional['Video'],
        video_note: Optional['VideoNote'],
        voice: Optional['Voice'],
        has_media_spoiler: Optional[bool],
        contact: Optional['Contact'],
        dice: Optional['Dice'],
        game: Optional['Game'],
        giveaway: Optional['Giveaway'],
        giveaway_winners: Optional['GiveawayWinners'],
        invoice: Optional['Invoice'],
        location: Optional['Location'],
        poll: Optional['Poll'],
        venue: Optional['Venue']
    ):
        self.origin = origin
        self.chat = chat
        self.message_id = message_id
        self.link_preview_options = link_preview_options
        self.animation = animation
        self.audio = audio
        self.document = document
        self.paid_media = paid_media
        self.photo = photo
        self.sticker = sticker
        self.story = story
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.invoice = invoice
        self.location = location
        self.poll = poll
        self.venue = venue
