import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://www.imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=RH57A2SWQDKQ8DF35GR5&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4")

bs = BeautifulSoup(page.content, 'lxml')

stars = bs.find('a', string='Stars').nextSibling()[0]
temp = [x.text for x in stars.findAll('a')]
print(temp)



