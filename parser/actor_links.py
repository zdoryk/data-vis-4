import requests
from bs4 import BeautifulSoup
import json
from numpy import linspace

file = open('america.json', 'r')



q = json.load(file)

sources = {}

q['nodes'] = q['nodes'][:50]

max_ = sorted(q['nodes'], key=lambda x: x['rating'], reverse=True)[0]['rating']
min_ = sorted(q['nodes'], key=lambda x: x['rating'], reverse=True)[-1]['rating']

lspace = linspace(min_, max_, 4)
lspace = list(lspace)
lspace.reverse()
colors_id = [x.lower() for x in ['#E76C53', '#EFD077', '#0099A9', '#00FCA8']]
colors_id.reverse()
colors = {}

print(colors_id)

for i in range(len(lspace)):
    colors[lspace[i]] = colors_id[i]

for node in q['nodes']:
    for rating, color in colors.items():
        if node['rating'] >= rating:
            node['color'] = color
            break

all_actors = []

for i in q['nodes']:
    all_actors = all_actors + i['actors']

all_actors = list(set(all_actors))

actors_dict = {}

for actor in all_actors:
    actors_dict[actor] = []

for i in q['nodes']:
    for k, v in actors_dict.items():
        if k in i['actors']:
            v.append(i['title'])

print(actors_dict)

all_sources = []

for k, v in actors_dict.items():
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


q['links'] = all_sources

print(q)

with open("json_nodes_with_links_actors.json", "w") as file:
    json.dump(q, file, indent=4)