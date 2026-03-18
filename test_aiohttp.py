import asyncio
import aiohttp
import traceback

async def test_ping():
    URL = "http://localhost:8080/" # or whatever URL is default
    print("Pinging:", URL)
    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=10)
        ) as session:
            async with session.get(URL) as resp:
                print("Pinged server with response: {}".format(resp.status))
    except TimeoutError:
        print("Couldn't connect to the site URL..!")
    except Exception:
        traceback.print_exc()

asyncio.run(test_ping())
