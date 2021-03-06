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

import asyncio
import typing

__all__ = (
    "REST_BASE_URL",
    "Route",
    "RatelimitHandler",
)

REST_BASE_URL = "https://discord.com/api/v10"


class Route:
    __slots__ = ("method", "path", "requires_auth", "params")

    def __init__(self,
        method: typing.Literal["GET", "POST", "PUT", "DELETE", "PATCH"],
        path: str,
        *,
        requires_auth: bool = True,
        **params: typing.Any,
    ) -> None:

        self.method = method
        self.path = path
        self.requires_auth = requires_auth
        self.params = params

    @property
    def url(self) -> str:
        return REST_BASE_URL + self.path.format_map(self.params)

    @property
    def ratelimit_path(self) -> str:
        params = self.params
        guild_id = params.get("guild_id")
        channel_id = params.get("channel_id")
        return f"{self.method}-{self.path}-{guild_id}:{channel_id}"

    def __repr__(self) -> str:
        return f"{self.method} {self.url}"


class RatelimitHandler:
    def __init__(self) -> None:
        # Lock for tracking global ratelimit
        self.global_ratelimit_cleared = asyncio.Event()
        self.global_ratelimit_cleared.set()

        # { bucket_hash | ratelimit_path : asyncio.Lock }
        self.locks: typing.Dict[str, asyncio.Lock] = {}

        # { ratelimit_path : bucket_hash }
        self.buckets: typing.Dict[str, str] = {}

    def clear(self) -> None:
        """Clears internal ratelimit data including locks and bucket hashes."""
        self.locks.clear()
        self.buckets.clear()

    def set_global(self) -> None:
        """Sets the global ratelimit, preventing any HTTP requests."""
        self.global_ratelimit_cleared.clear()

    def reset_global(self) -> None:
        """Resets the global ratelimit, awakening the waiter coroutines."""
        self.global_ratelimit_cleared.set()

    async def wait_until_global_reset(self) -> None:
        """Blocks until global ratelimit is cleared."""
        await self.global_ratelimit_cleared.wait()

    def get_lock(self, path: str) -> asyncio.Lock:
        """Gets the asyncio.Lock instance for given route's path."""

        # Firstly, try to retrieve the bucket hash for this path.
        key = self.buckets.get(path)

        if key is None:
            # Bucket hash not found, As a workaround, we will be falling
            # back to storing lock with the route's path.
            key = path

        try:
            return self.locks[key]
        except KeyError:
            self.locks[key] = lock = asyncio.Lock()
            return lock

    def set_bucket(self, path: str, bucket: str) -> None:
        """Stores the bucket hash for the given route's path."""

        # If we have a "fallback" lock stored in the locks mapping with
        # the route's path, We want to store that lock with the bucket hash
        # as key and remove the route's path from the mapping.
        try:
            lock = self.locks.pop(path)
        except KeyError:
            pass
        else:
            self.locks[bucket] = lock

        self.buckets[path] = bucket
