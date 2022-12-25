import asyncio
import aiohttp
# import requests
import time


async def download_site(url, session):
    async with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

# def download_all_sites(sites):
#     with requests.session() as session:
#         for url in sites:
#             download_site(url, session)


def main():
    sites = [
                "https://www.jython.org",
                "https://python.org/",
            ]
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(80):
            for url in sites:
                task = asyncio.create_task(download_site(url, session))
                tasks.append(task)

        await asyncio.gather(*tasks)
        # print(f"Downloaded {len(sites)} in {duration} seconds")


if __name__ == '__main__':
    # sites = [
    #             "https://www.jython.org",
    #             "https://python.org/",
    #         ] * 80
    start_time = time.time()
    asyncio.run(main())
    # download_all_sites(sites)
    duration = time.time() - start_time
