# -*- coding: utf-8 -*-
import stage
import asyncio

stage = stage.Stage()

async def main():
    running = True
    while running:
        running = stage.run()
        await asyncio.sleep(0)

asyncio.run(main())