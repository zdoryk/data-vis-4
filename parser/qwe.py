import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

test = {}
temp = []

if page.status_code == 200:
    bs = BeautifulSoup(page.content, 'lxml')
    # print(bs)
    temp = [x.text.strip().replace('\n', '') for x in bs.find("ul", {"class": "quicklinks"}).findAll('a')]
    # print(temp)

for i in temp:
    test[i] = []

print(test)

file = open('america.json', 'r')

q = json.load(file)

sources = {}

for i in q['nodes'][:10]:
    for k, v in test.items():
        if k in i['genres']:
            v.append(i['title'])

all_sources = []

for k, v in test.items():
    # print(v)
    for source in v:
        for target in v:
            if source != target:
                all_sources.append(
                    {
                        'source': source,
                        'target': target,
                        'value': 1
                    }
                )

print(all_sources)
q['links'] = all_sources

print(q)

with open("json_nodes_with_links_a.json", "w") as file:
    json.dump(q, file, indent=4)