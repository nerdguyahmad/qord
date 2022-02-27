# MIT License

# Copyright (c) 2022 Izhar Ahmad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations


class GatewayEvent:
    r"""An enumeration that details names of various events sent over gateway.

    These events names are commonly passed in :class:`Client.event` decorator for
    registering a listener for relevant event.
    """

    GATEWAY_DISPATCH = "gateway_dispatch"
    r"""Called whenever gateway sends a dispatch event. See :class:`events.GatewayDispatch` for more info."""

    SHARD_READY = "shard_ready"
    r"""Called whenever a shard is in ready state. See :class:`events.ShardReady` for more info."""

    READY = "ready"
    r"""Called whenever all shards are ready. See :class:`events.Ready` for more info."""

    GUILD_AVAILABLE = "guild_available"
    r"""Called whenever a guild becomes available to the client. See :class:`events.GuildAvailable` for more info."""

    GUILD_UNAVAILABLE = "guild_unavailable"
    r"""Called whenever a guild becomes unavailable to the client. See :class:`events.GuildUnavailable` for more info."""

    GUILD_JOIN = "guild_join"
    r"""Called whenever the bot joins a new guild. See :class:`events.GuildJoin` for more info."""

    GUILD_LEAVE = "guild_leave"
    r"""Called whenever the bot leaves a guild. See :class:`events.GuildLeave` for more info."""

    GUILD_UPDATE = "guild_update"
    r"""Called whenever a guild is updated. See :class:`events.GuildUpdate` for more info."""

    ROLE_CREATE = "role_create"
    r"""Called whenever a guild role is created. See :class:`events.RoleCreate` for more info."""

    ROLE_UPDATE = "role_update"
    r"""Called whenever a guild role is updated. See :class:`events.RoleUpdate` for more info."""

    ROLE_DELETE = "role_delete"
    r"""Called whenever a guild role is deleted. See :class:`events.RoleDelete` for more info."""

    GUILD_MEMBER_ADD = "guild_member_join"
    r"""Called whenever a member joins a guild. See :class:`events.GuildMemberAdd` for more info."""

    GUILD_MEMBER_REMOVE = "guild_member_remove"
    r"""Called whenever a member is removed i.e left, kicked or banned from a guild. See :class:`events.GuildMemberRemove` for more info."""

    GUILD_MEMBER_UPDATE = "guild_member_update"
    r"""Called whenever a member is updated. See :class:`events.GuildMemberUpdate` for more info."""

    CHANNEL_CREATE = "channel_create"
    r"""Called whenever a channel is created. See :class:`events.ChannelCreate` for more info."""

    CHANNEL_UPDATE = "channel_update"
    r"""Called whenever a channel is updated. See :class:`events.ChannelUpdate` for more info."""

    CHANNEL_DELETE = "channel_delete"
    r"""Called whenever a channel is deleted. See :class:`events.ChannelDelete` for more info."""

class PremiumType:
    r"""An enumeration that details values for a user's premium aka nitro subscription.

    Most common place where this enumeration is useful is when working with the
    :attr:`User.premium_type` attribute.
    """

    NONE = 0
    r"""User has no nitro subcription."""

    NITRO_CLASSIC = 1
    r"""User has nitro classic subscription."""

    NITRO = 2
    r"""User has nitro subscription."""

class DefaultAvatar:
    r"""An enumeration that details values for a user's default avatar.

    A user's default avatar value is calculated on the basis of user's
    four digits discriminator. It can be generated by::

        default_avatar = int(user.discriminator) % DefaultAvatar.INDEX

    To get a user's default avatar value, You should use :attr:`User.default_avatar`
    attribute.
    """

    BLURPLE = 0
    r"""Blurple coloured default avatar."""

    GRAY = 1
    r"""Gray coloured default avatar."""

    GREEN = 2
    r"""Green coloured default avatar."""

    YELLOW = 3
    r"""Yellow coloured default avatar."""

    RED = 4
    r"""Red coloured default avatar."""

    PINK = 5
    r"""Pink coloured default avatar."""

    INDEX = 5
    r"""The zero based index integer used for generating the user's default avatar.

    This is based of number of colours available for default avatars.
    As such, If Discord adds a new avatar colour, This index will increment.
    """

class ImageExtension:
    r"""An enumeration that details values for a various image extensions supported
    on the Discord CDN URLs.
    """

    PNG = "png"
    r"""PNG extension."""

    JPG = "jpg"
    r"""An alias of :attr:`.JPEG`."""

    JPEG = "jpeg"
    r"""JPEG extension."""

    WEBP = "webp"
    r"""WEBP extension."""

    GIF = "gif"
    r"""GIF extension. This is only supported for animated image resources."""

class VerificationLevel:
    r"""An enumeration that details values for a :class:`Guild`'s :attr:`~Guild.verification_level`

    Verification level defines the requirements for a user account to be member of the guild.
    """

    NONE = 0
    r"""No verification level set. Unrestricted."""

    LOW = 1
    r"""Users must have verified email bound to their account."""

    MEDIUM = 2
    r"""Users must also be registered to Discord for more then 5 minutes."""

    HIGH = 3
    r"""Users must also be part of the guild for more then 10 minutes."""

    VERY_HIGH = 4
    r"""Users must also have a verified phone number bound to their account."""

class NotificationLevel:
    r"""An enumeration that details values for a :class:`Guild`'s :attr:`~Guild.notification_level`

    Notification level defines the levels of notifications that the members of the
    guilds will receive upon messages.
    """

    ALL_MESSAGES = 0
    r"""Members will receive notifications for every single message sent in the guild."""

    ONLY_MENTIONS = 1
    r"""Members will receive notifications for only messages that mentions them."""

class ExplicitContentFilter:
    r"""An enumeration that details values for a :class:`Guild`'s :attr:`~Guild.explicit_content_filter`

    Explicit content filter defines the explicit content checks and filters done on the files
    sent in the guild messages.
    """

    DISABLED = 0
    r"""No scanning on sent files will be done."""

    MEMBERS_WITHOUT_ROLES = 1
    r"""Scanning will be done for messages sent by members that don't have any role assigned."""

    ALL_MEMBERS = 2
    r"""Scanning will be done for all messages."""

class NSFWLevel:
    r"""An enumeration that details values for a :class:`Guild`'s :attr:`~Guild.nsfw_level`

    NSFW level defines whether the guild is marked as Not Safe For Work (NSFW) or
    age restricted.
    """

    DEFAULT = 0
    r"""No explicit NSFW level is set."""

    EXPLICIT = 1
    r"""Guild is marked as explicit."""

    SAFE = 2
    r"""Guild is marked as Safe For Work (SFW)."""

    AGE_RESTRICTED = 3
    r"""Guild is marked as age restricted."""

class PremiumTier:
    r"""An enumeration that details values for a :class:`Guild`'s :attr:`~Guild.premium_tier`

    Premium tier defines the server boosts level of the guild.
    """

    NONE = 0
    r"""No boost level unlocked by the guild yet."""

    TIER_1 = 1
    r"""Guild has unlocked boost level 1 perks."""

    TIER_2 = 2
    r"""Guild has unlocked boost level 2 perks."""

    TIER_3 = 3
    r"""Guild has unlocked boost level 3 perks."""

class MFALevel:
    r"""An enumeration that details values for a :class:`Guild`'s :attr:`~Guild.mfa_level`

    MFA level defines the 2 factor authentication requirement for the guild moderators
    for performing moderative actions.
    """

    DISABLED = 0
    r"""2FA is not required for performing moderative actions."""

    ELEVATED = 1
    r"""2FA is required for performing moderative actions.."""

class ChannelType:
    r"""An enumeration that details the types of channels."""

    TEXT = 0
    r"""The channel is a guild's text channel."""

    DIRECT = 1
    r"""The channel is a private DM between two users."""

    VOICE = 2
    r"""The channel is a guild's voice channel."""

    GROUP = 3
    r"""The channel is a private group DM channel."""

    CATEGORY = 4
    r"""The channel is a guild's category that holds other channels."""

    NEWS = 5
    r"""The channel is a guild's news channel."""

    STORE = 6
    r"""The channel is a guild's store channel."""

    NEWS_THREAD = 10
    r"""The channel is a thread created inside a news channel."""

    PUBLIC_THREAD = 11
    r"""The channel is a public thread."""

    PRIVATE_THREAD = 12
    r"""The channel is a private thread."""

    STAGE = 13
    r"""The channel is a guild's stage channel."""

class VideoQualityMode:
    r"""An enumeration that details the video quality mode of a :class:`VoiceChannel`."""

    AUTO = 1
    r"""Automatic quality. Discord will chose the best quality for optimal performance."""

    FULL = 2
    r"""720p quality."""
