import asyncio
import time
import aiohttp
import ssl
import certifi
""" 
function download_image(url):
    get data from url
    open file
    write data
    close file
"""

async def download_image(session, url, filename):
    async with session.get(url) as response:
        if response.status == 200:
            image_bytes = await response.read()
            with open(filename, "wb") as file:
                file.write(image_bytes)
            print(f"{filename} saved successfully")
        else:
            print(f"failed to download{url}")


async def main():
    image_urls = [
        "https://picsum.photos/200/300",
        "https://picsum.photos/300/300",
        "https://picsum.photos/400/300",
        "https://picsum.photos/500/300",
    ]
    start_time = time.time()
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
    
        tasks = []
        for ind, url in enumerate(image_urls, start = 1):
            filename = rf"C:\Users\PranavMangal\Desktop\Python my work deep dive\AsyncIO\Images\image_{ind}.jpg"
            task = download_image(session, url, filename)
            tasks.append(task)
        await asyncio.gather(*tasks)
        
    end_time = time.time()

    print(f"Total time taken is {end_time - start_time:.2f} seconds")


asyncio.run(main())
