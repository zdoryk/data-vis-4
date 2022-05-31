from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import json
from time import time

start_time = time()
root_url = 'https://www.imdb.com/'

a_tags = []
all_films = []


async def get_page_data(session, url: str):
    async with session.get(url) as re:
        # print(1)
        film = BeautifulSoup(await re.text(), "lxml")
        try:
            rating = film.find(text='IMDb RATING').findNext('a').find('span').text
        except:
            rating = 0

        try:
            genres = [x.text for x in film.find("div", {'data-testid': 'genres'})]
        except:
            genres = ['[]']

        try:
            title = film.find("h1").text
        except:
            title = 'Title'

        try:
            temp = film.find("ul", {"data-testid": "hero-title-block__metadata"}).findAll('li')[2].text.split()
            time = int(temp[0][0]) * 60 + int(temp[1][:2])
        except:
            time = 0

        all_films.append(
            {
                'title': title,
                'rating': rating,
                'genres': genres,
                'time': time
            }
        )


async def load_site_data():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for a in a_tags:
            task = asyncio.create_task(get_page_data(session, root_url + a))
            tasks.append(task)
        await asyncio.gather(*tasks)
    await session.close()


def start():
    page = requests.get("https://www.imdb.com/chart/top/")
    global a_tags

    if page.status_code == 200:
        bs = BeautifulSoup(page.content, 'html.parser')

        data = bs.find("table", {"class": "chart full-width"}).findAll("a")

        a_tags = [str(x)[10:26] for x in data]
        a_tags = a_tags[1::2]

    asyncio.get_event_loop().run_until_complete(load_site_data())
    # asyncio.run(load_site_data())

    for_dump = sorted(all_films, key=lambda x: x['rating'], reverse=True)
    for_dump = {"nodes": for_dump}
    print(for_dump)

    with open("america.json", "w") as file:
        json.dump(for_dump, file, indent=4)

    print(f'Execution time: {time() - start_time}')


start()
