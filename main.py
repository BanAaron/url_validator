import csv
import asyncio
import aiohttp


async def fetch_url(session, url):
    try:
        async with session.head(url) as response:
            return url, response.status, url.replace("cardigasounn", "cardigan")
    except Exception as e:
        return url, None, None


async def main():
    urls = []
    with open("urls") as urls_file:
        urls = urls_file.readlines()

    results = []

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url.strip()) for url in urls]
        results = await asyncio.gather(*tasks)

    with open("results.csv", "w") as write_file:
        writer = csv.writer(write_file)
        writer.writerow(["url", "response_code", "new_url"])
        for result in results:
            writer.writerow(result)


if __name__ == '__main__':
    asyncio.run(main())
