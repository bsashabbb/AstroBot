from __future__ import annotations
from typing import Optional, List, Union

class ExternalReplyInfo:
    def __init__(
        self,
        origin: 'MessageOrigin',
        chat: 'Optional[Chat]' = None,
        message_id: 'Optional[int]' = None,
        link_preview_options: 'Optional[LinkPreviewOptions]' = None,
        animation: 'Optional[Animation]' = None,
        audio: 'Optional[Audio]' = None,
        document: 'Optional[Document]' = None,
        paid_media: 'Optional[PaidMediaInfo]' = None,
        photo: 'Optional[List[PhotoSize]]' = None,
        sticker: 'Optional[Sticker]' = None,
        story: 'Optional[Story]' = None,
        video: 'Optional[Video]' = None,
        video_note: 'Optional[VideoNote]' = None,
        voice: 'Optional[Voice]' = None,
        has_media_spoiler: 'Optional[bool]' = None,
        contact: 'Optional[Contact]' = None,
        dice: 'Optional[Dice]' = None,
        game: 'Optional[Game]' = None,
        giveaway: 'Optional[Giveaway]' = None,
        giveaway_winners: 'Optional[GiveawayWinners]' = None,
        invoice: 'Optional[Invoice]' = None,
        location: 'Optional[Location]' = None,
        poll: 'Optional[Poll]' = None,
        venue: 'Optional[Venue]' = None
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