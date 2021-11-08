print('#1')
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

print ('#2')
from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            text = await resp.text()
            C=eval(text)
            print(C[service[2]])
    # получение ip


async def asynchronous():
    # TODO:
    # создание футур для сервисов
    # используйте FIRST_COMPLETED
    fut = asyncio.ensure_future(fetch_ip(SERVICES[0]))
    fut1 = asyncio.ensure_future(fetch_ip(SERVICES[1]))
    await asyncio.wait([fut, fut1], return_when=FIRST_COMPLETED)


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())