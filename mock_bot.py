import sys
import asyncio
from unittest.mock import AsyncMock, MagicMock

sys.modules['pyrogram'] = MagicMock()
sys.modules['pyrogram'].Client = MagicMock
sys.modules['pyrogram'].idle = AsyncMock()

# We can just import dreamxbotz_start from bot and replace the client start
import bot
bot.dreamxbotz.start = AsyncMock()
bot.dreamxbotz.get_me = AsyncMock(return_value=MagicMock(username="test_bot", id=123, first_name="Test", mention="test"))
bot.initialize_clients = AsyncMock()
bot.db.get_banned = AsyncMock(return_value=([], []))
bot.Media.ensure_indexes = AsyncMock()
bot.Media2.ensure_indexes = AsyncMock()
bot.dreamxbotz.send_message = AsyncMock()

async def main():
    try:
        await bot.dreamxbotz_start()
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(main())
