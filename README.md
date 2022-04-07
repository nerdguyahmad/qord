
# Qord

<div>
  <img src="https://img.shields.io/discord/940601074031677448?color=%234069e2&label=Discord">
  <img src="https://img.shields.io/pypi/dm/qord?color=%233674a5">
  <img src="https://img.shields.io/github/commit-activity/w/nerdguyahmad/qord">
</div><br>

Python library for Discord API based around asyncio.

**Features:**

- Object oriented, user friendly interface with no dirty payloads.
- Easy to customise and manage.
- Robust handling of HTTP ratelimits.
- Supports automatic gateway sharding.

## Development stage
Qord is currently under it's initial development (alpha) stage. During this phase, There may be breaking changes and public user-facing API should not be considered stable. There would be no efforts in keeping backward compatibility. While the library currently supports the basic functionalities required to build a bot, many essential features are yet to be implemented and for this reason, Qord isn't yet a library to choose for making full fledged bots.

The complete lifetime of 0.x version is considered the development phase. More info about this [semantic versioning specification is here](https://semver.org/#spec-item-4)

## Installation
Qord is installed using Python's traditional package manager, pip.
```bash
pip install -U qord
```
> ℹ️ On Windows and Mac, you might need to prefix the above command with `python -m` for it work.

Qord requires **Python 3.8 or higher.** The dependencies are handled by pip automatically, See complete list of dependencies in [here](https://github.com/nerdguyahmad/qord/blob/main/requirements.txt).

## Usage
To whet your appetite, Let's get a quickstart with an example of a simple "Ping-Pong" bot.
```py
import qord

intents = qord.Intents.unprivileged()
intents.message_content = True
client = qord.Client(intents=intents)

@client.event(qord.GatewayEvent.READY)
async def on_ready(event):
  print("Bot is ready.")
  print(f"Shards: {client.shards_count}")
  print(f"User: {client.user.proper_name}")
  print(f"Guilds: {len(client.cache.guilds())}")

@client.event(qord.GatewayEvent.MESSAGE_CREATE)
async def on_message_create(event):
  message = event.message

  if message.author.bot:
    # Don't respond to bot messages.
    return

  if message.content == "!ping":
    await message.channel.send("Pong!")

client.start("BOT_TOKEN")
```

For a brief explanation of this example, see [it's explanation](https://github.com/nerdguyahmad/qord/blob/master/examples/basic.py). More examples in the [`examples`](https://github.com/nerdguyahmad/qord/blob/master/examples) directory.

## Contributing
Qord is under heavy development. You can help us in reaching 100% coverage of Discord API by reporting bugs, suggesting features or even directly contributing to the code base, See [Contribution Guidelines](https://github.com/nerdguyahmad/qord/blob/main/CONTRIBUTING.MD).

----

<br>
<div align="center">
  <a href="https://qord.rtfd.io">Documentation</a> • <a href="https://discord.gg/nE9cGtzayA">Discord Server</a> • <a href="https://pypi.org/project/qord">PyPi</a>
  • <a href="https://github.com/nerdguyahmad/qord">GitHub</a> • <a href="https://github.com/nerdguyahmad/qord/issues">Issues Tracker</a>
  <br><br>
  <sup>Copyright (C) nerdguyahmad and contributors 2022, Under the MIT license.</sup>
</p>
