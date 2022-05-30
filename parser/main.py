from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp
import json

# def worker(url):
#     re = requests.get(root_link + url)
#     film = BeautifulSoup(re.content, 'html.parser')
#     rating = film.find("span", {"class": "sc-7ab21ed2-1 jGRxWM"}).text
#     genres_raw = film.find("div", {"class": "ipc-chip-list sc-16ede01-4 bMBIRz"}).findAll('li')
#     genres = [x.text for x in genres_raw]
#     title = film.find("h1").text
#     all_films.append([title, rating, genres])
#     # print(all_films)

async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(root_link + url, headers=headers) as resp:
            return await resp.text()

async def get_page_data(session, a):
    url = root_link + a

    async with session.get(url=url, headers=headers) as response:
        response_text = await response.text()
        film = BeautifulSoup(re.content, 'lxml')

        rating = film.find("span", {"class": "sc-7ab21ed2-1 jGRxWM"}).text
        genres_raw = film.find("div", {"class": "ipc-chip-list sc-16ede01-4 bMBIRz"}).findAll('li')
        genres = [x.text for x in genres_raw]
        title = film.find("h1").text
        all_films.append([title, rating, genres])
        print(all_films)
        print(str(index) + f'/{len(a)}')


root_link = 'https://www.imdb.com/'

headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }


page = requests.get("https://www.imdb.com/chart/top/")

if page.status_code == 200:
    bs = BeautifulSoup(page.content, 'html.parser')

    data = bs.find("table", {"class": "chart full-width"}).findAll("a")

    a = [str(x)[10:26] for x in data]
    a = a[1::2]
    a = a[:50]

    all_films = []
    counter = 0
    for index, i in enumerate(a):
        re = requests.get(root_link + i)
        film = BeautifulSoup(re.content, 'html.parser')
        # rating = film.find(text='IMDb RATING').findNext('a').find('span').text
        # genres = [x.text for x in film.find("div", {'data-testid': 'genres'})]
        # genres = [x.text for x in genres_raw]
        title = film.find("h1").text
        # all_films.append([title, rating, genres])
        print(genres)
        print(str(index) + f'/{len(a)}')

else:
    print(page.status_code, BeautifulSoup(page.content,'html.parser'))



if __name__ == '__main__':
    pass

