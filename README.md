# Cog reloader
Make reloading cogs easy while editing. Compitable with `nextcord` and `discord.py`

# Warning
- Don't load this while bot is in production, Load only in development environment.
- This will not reload files that are not cog.

# Installation
`pip install cog-reloader`

# Usage

```python
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.load_extension('cog_reloader') # make sure its an `_` not `-`

TOKEN = 'TOKEN_HERE'
bot.run(TOKEN)
```

[Join Discord](https://discord.gg/7SaE8v2) For any kind of help