1. *Identify the cause of the Render crash.*
   - The bot crashes and fails to respond to UptimeRobot pings.
   - Investigate blocking calls like `time.sleep` or synchronous IO that block the event loop, preventing `aiohttp` from responding to pings on Render.
   - Investigate synchronous `imdb` calls that can block the loop or crash if they timeout/fail.
   - Investigate `ping_server` or `keep_alive` tasks to see if they block.
2. *Fix blocking `time.sleep` calls.*
   - Replace any `time.sleep(e.value)` or `sleep` imported from `time` with `await asyncio.sleep(e.value)`.
3. *Fix blocking IMDb network calls.*
   - `imdb.search_movie` and `imdb.get_movie` from `cinemagoer` are synchronous and block the event loop. This leads to the main loop failing to handle `aiohttp` requests or keep-alive pings on Render, causing 503 errors and hibernation.
   - Move these synchronous IMDb calls to `asyncio.to_thread` so they run in a separate thread and don't block the main event loop.
4. *Verify changes.*
   - Ensure the bot starts and the event loop isn't blocked by IMDb lookups.
5. *Pre-commit steps and submit.*
   - Run the pre-commit instructions and then use the `submit` tool to save changes.
