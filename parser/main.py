import requests
from bs4 import BeautifulSoup
import json

headers = {}

page = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

bs = BeautifulSoup(page.content, 'lxml')





