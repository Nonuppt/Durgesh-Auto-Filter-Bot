import asyncio
from unittest.mock import MagicMock
import utils

# Mock the cinemagoer so it doesn't do real requests in test but let's see if asyncio.to_thread is called right
async def main():
    try:
        await utils.get_poster('Inception')
        print("Success!")
    except Exception as e:
        print(e)

asyncio.run(main())
