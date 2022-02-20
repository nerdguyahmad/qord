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

from qord.models.base import BaseModel
from qord.models.users import User
from qord._helpers import parse_iso_timestamp
from datetime import datetime

import typing

if typing.TYPE_CHECKING:
    from qord.models.roles import Role
    from qord.models.guilds import Guild

T = typing.TypeVar("T")

class GuildMember(BaseModel):
    r"""Representation of a guild member.

    A guild member is simply a user that is part of a specific :class:`Guild`. This
    class bundles the properties associated to a guild member. To access the actual
    user associated to this member, you should consider using :attr:`.user` attribute.

    Attributes
    ----------
    guild: :class:`Guild`
        The parent guild that this member belongs to.
    user: :class:`User`
        The user associated to this member.
    nickname: Optional[:class:`builtins.str`]
        The nickname of this member in the guild. If member has no guild
        specific nickname set, This is ``None``. See :attr:`.display_name` property
        that aids in retrieving the name more efficiently.
    avatar: Optional[:class:`builtins.str`]
        The hash of avatar for this member in the guild. If member has no
        guild specific avatar set, This is ``None``. See :attr:`.display_avatar` property
        that aids in retrieving the avatar more efficiently.
    deaf: :class:`builtins.bool`
        Whether the member is deafened in voice channels.
    mute: :class:`builtins.bool`
        Whether the member is muted in voice channels.
    pending: :class:`builtins.bool`
        Whether the member has passed the membership screening.
    joined_at: :class:`datetime.datetime`
        The time when member joined the guild.
    premium_since: Optional[:class:`datetime.datetime`]
        The time when member started boosting the guild if applicable. If member
        is not boosting the guild, This is ``None``.
    timeout_until: Optional[:class:`datetime.datetime`]
        The time until which member is timed out and cannot interact with
        the guild. If member is not timed out, This is ``None``.

        .. note::
            This attribute may have a value set even if member is not actually
            timed out. In which case, The datetime object would be in past. See
            :meth:`.is_timed_out` check that covers all possible cases.

    role_ids: List[:class:`builtins.int`]
        The list of IDs of roles that are associated to this member.
    roles: List[:class:`Role`]
        The list of roles associated to this member.
    """
    if typing.TYPE_CHECKING:
        guild: Guild
        user: User
        nickname: typing.Optional[str]
        avatar: typing.Optional[str]
        deaf: bool
        mute: bool
        pending: bool
        joined_at: datetime
        premium_since: typing.Optional[datetime]
        timeout_until: typing.Optional[datetime]
        role_ids: typing.List[int]
        roles: typing.List[Role]

    __slots__ = ("guild", "_client", "user", "nickname", "avatar", "deaf", "mute", "pending",
                "joined_at", "premium_since", "timeout_until", "role_ids", "roles")

    def __init__(self, data: typing.Dict[str, typing.Any], guild: Guild) -> None:
        self.guild = guild
        self._client = guild._client
        self._update_with_data(data)

    def _update_with_data(self, data: typing.Dict[str, typing.Any]) -> None:
        self.user = user = User(data["user"], client=self._client)
        self.nickname = data.get("nick")
        self.avatar = data.get("avatar")
        self.deaf = data.get("deaf", False)
        self.mute = data.get("mute", False)
        self.pending = data.get("pending", False)

        premium_since = data.get("premium_since")
        timeout_until = data.get("communication_disabled_until")

        self.joined_at = parse_iso_timestamp(data["joined_at"])
        self.premium_since = parse_iso_timestamp(premium_since) if premium_since is not None else None
        self.timeout_until = parse_iso_timestamp(timeout_until) if timeout_until is not None else None

        role_ids = [int(role_id) for role_id in data.get("roles", [])]
        roles = []
        guild = self.guild

        for role_id in role_ids:
            role = guild.cache.get_role(role_id)
            roles.append(role)

        self.role_ids = role_ids
        self.roles = roles

    @property
    def display_name(self) -> str:
        r"""Returns the name of this member as displayed in the guild.

        This property would return the :attr:`.nickname` of the member if it's present
        and would fallback to :attr:`User.name` if nickname is not available.

        Returns
        -------
        :class:`builtins.str`
        """
        nick = self.nickname
        if nick is not None:
            return nick
        return self.user.name

    @property
    def display_avatar(self) -> typing.Optional[str]:
        r"""Returns the avatar's hash of this member as displayed in the guild.

        This property would return the :attr:`.avatar` of this member if available
        and would fallback to :attr:`User.avatar` when unavailable. If user has no
        avatar set, ``None`` would be returned.

        Returns
        -------
        Optional[:class:`builtins.str`]
        """
        avatar = self.avatar
        if avatar is not None:
            return avatar
        return self.user.avatar

    def is_avatar_animated(self, guild_only: bool = False) -> bool:
        r"""Checks whether the member's avatar is animated.

        When ``guild_only`` is ``True``, Checks for only the guild's
        :attr:`.avatar`. Otherwise checks if for the :attr:`.display_avatar`
        i.e either one of guild avatar or associated :attr:`.user` avatar
        is animated.

        Parameters
        ----------
        guild_only: :class:`builtins.bool`
            Whether to check for guild specific avatar only. Defaults
            to ``False``.

        Returns
        -------
        :class:`builtins.bool`
        """
        avatar = self.avatar

        if guild_only:
            if avatar is None:
                return False
            return avatar.startswith("a_")

        display_avatar = self.display_avatar

        if display_avatar is None:
            return False

        return display_avatar.startswith("a_")

    def is_boosting(self) -> bool:
        r"""Checks whether the member is boosting the guild.

        Returns
        -------
        :class:`builtins.bool`
        """
        return self.premium_since is not None

    def is_timed_out(self) -> bool:
        r"""Checks whether the member is timed out.

        Returns
        -------
        :class:`builtins.bool`
        """
        timeout_until = self.timeout_until
        if timeout_until is None:
            return False
        now = datetime.now()
        return now < timeout_until