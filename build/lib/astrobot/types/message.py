from __future__ import annotations
from typing import Optional, List, Union, Any

class Message:
    """Message Telegram API type"""

    def __init__(
        self,
        message_id: int,
        message_thread_id: Optional[int],
        from_user: Optional['User'],
        sender_chat: Optional['Chat'],
        sender_boost_count: Optional[int],
        sender_business_bot: Optional['User'],
        date: int,
        business_connection_id: Optional[str],
        chat: 'Chat',
        forward_origin: Optional['MessageOrigin'],
        is_topic_message: Optional[bool],
        is_automatic_forward: Optional[bool],
        reply_to_message: Optional['Message'],
        external_reply: Optional['ExternalReplyInfo'],
        quote: Optional['TextQuote'],
        reply_to_story: Optional['Story'],
        via_bot: Optional['User'],
        edit_date: Optional[int],
        has_protected_content: Optional[bool],
        is_from_offline: Optional[bool],
        media_group_id: Optional[str],
        author_signature: Optional[str],
        text: Optional[str],
        entities: Optional[List['MessageEntity']],
        link_preview_options: Optional['LinkPreviewOptions'],
        effect_id: Optional[str],
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
        caption: Optional[str],
        caption_entities: Optional[List['MessageEntity']],
        show_caption_above_media: Optional[bool],
        has_media_spoiler: Optional[bool],
        contact: Optional['Contact'],
        dice: Optional['Dice'],
        game: Optional['Game'],
        poll: Optional['Poll'],
        venue: Optional['Venue'],
        location: Optional['Location'],
        new_chat_members: Optional[List['User']],
        left_chat_member: Optional['User'],
        new_chat_title: Optional[str],
        new_chat_photo: Optional[List['PhotoSize']],
        delete_chat_photo: Optional[bool],
        group_chat_created: Optional[bool],
        supergroup_chat_created: Optional[bool],
        channel_chat_created: Optional[bool],
        message_auto_delete_timer_changed: Optional['MessageAutoDeleteTimerChanged'],
        migrate_to_chat_id: Optional[int],
        migrate_from_chat_id: Optional[int],
        pinned_message: Optional['MaybeInaccessibleMessage'],
        invoice: Optional['Invoice'],
        successful_payment: Optional['SuccessfulPayment'],
        refunded_payment: Optional['RefundedPayment'],
        users_shared: Optional['UsersShared'],
        chat_shared: Optional['ChatShared'],
        connected_website: Optional[str],
        write_access_allowed: Optional['WriteAccessAllowed'],
        passport_data: Optional['PassportData'],
        proximity_alert_triggered: Optional['ProximityAlertTriggered'],
        boost_added: Optional['ChatBoostAdded'],
        chat_background_set: Optional['ChatBackground'],
        forum_topic_created: Optional['ForumTopicCreated'],
        forum_topic_edited: Optional['ForumTopicEdited'],
        forum_topic_closed: Optional['ForumTopicClosed'],
        forum_topic_reopened: Optional['ForumTopicReopened'],
        general_forum_topic_hidden: Optional['GeneralForumTopicHidden'],
        general_forum_topic_unhidden: Optional['GeneralForumTopicUnhidden'],
        giveaway_created: Optional['GiveawayCreated'],
        giveaway: Optional['Giveaway'],
        giveaway_winners: Optional['GiveawayWinners'],
        giveaway_completed: Optional['GiveawayCompleted'],
        video_chat_scheduled: Optional['VideoChatScheduled'],
        video_chat_started: Optional['VideoChatStarted'],
        video_chat_ended: Optional['VideoChatEnded'],
        video_chat_participants_invited: Optional['VideoChatParticipantsInvited'],
        web_app_data: Optional['WebAppData'],
        reply_markup: Optional['InlineKeyboardMarkup']
    ):
        self.message_id = message_id
        self.message_thread_id = message_thread_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.sender_boost_count = sender_boost_count
        self.sender_business_bot = sender_business_bot
        self.date = date
        self.business_connection_id = business_connection_id
        self.chat = chat
        self.forward_origin = forward_origin
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.external_reply = external_reply
        self.quote = quote
        self.reply_to_story = reply_to_story
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.is_from_offline = is_from_offline
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.link_preview_options = link_preview_options
        self.effect_id = effect_id
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
        self.caption = caption
        self.caption_entities = caption_entities
        self.show_caption_above_media = show_caption_above_media
        self.has_media_spoiler = has_media_spoiler
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = message_auto_delete_timer_changed
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.refunded_payment = refunded_payment
        self.users_shared = users_shared
        self.chat_shared = chat_shared
        self.connected_website = connected_website
        self.write_access_allowed = write_access_allowed
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.boost_added = boost_added
        self.chat_background_set = chat_background_set
        self.forum_topic_created = forum_topic_created
        self.forum_topic_edited = forum_topic_edited
        self.forum_topic_closed = forum_topic_closed
        self.forum_topic_reopened = forum_topic_reopened
        self.general_forum_topic_hidden = general_forum_topic_hidden
        self.general_forum_topic_unhidden = general_forum_topic_unhidden
        self.giveaway_created = giveaway_created
        self.giveaway = giveaway
        self.giveaway_winners = giveaway_winners
        self.giveaway_completed = giveaway_completed
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup
