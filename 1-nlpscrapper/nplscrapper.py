from bs4 import BeautifulSoup
import os, requests

#bajo la pagina y la cargo en beautifulsoup
page = requests.get("https://kotaku.com")
soup = BeautifulSoup(page.content, "html.parser")
#busco links a las notas. fugly, but it works
curationMountainDiv = soup.find('div', {'class': 'js_curation-mountain curation-mountain Equal'})
linksParaScrappear = []
for i in curationMountainDiv.find_all('div', {'class':'curation-module__item js_curation-item box'}):
    linksParaScrappear.append(i.get('data-permalink'))

#scrapeo las primeras 3 notas
for i in linksParaScrappear[0:3]:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, "html.parser")
    curationMountainDiv = soup.find('div', {'class', 'post-content entry-content js_entry-content'}).text
    #brujeria que borra emptylines https://stackoverflow.com/questions/1140958/whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
    curationMountainDiv  = os.linesep.join([s for s in curationMountainDiv.splitlines() if s])
    print('----------------------------------------------------------------------------------------')
    print(curationMountainDiv)
    print('----------------------------------------------------------------------------------------')
