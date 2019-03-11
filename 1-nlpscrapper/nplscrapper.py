from bs4 import BeautifulSoup
import os

soup = BeautifulSoup(open("./kotaku.html"), "html.parser")
#busco links a las notas
curationMountainDiv = soup.find('div', {'class': 'js_curation-mountain curation-mountain Equal'})
for i in curationMountainDiv.find_all('div', {'class':'curation-module__item js_curation-item box'}):
    linksParaScrappear = i.get('data-permalink')




### Falta meter adentro de un FOR con los primeros 3 resultados de arriba
### Falta cambiar los BeautifulSoup de texto a wget o similar pythonezco

soup = BeautifulSoup(open("./kotaku2.html"), "html.parser")
#scrapeo las notas
curationMountainDiv = soup.find('div', {'class', 'post-content entry-content js_entry-content'}).text
#brujeria que borra emptylines https://stackoverflow.com/questions/1140958/whats-a-quick-one-liner-to-remove-empty-lines-from-a-python-string
curationMountainDiv  = os.linesep.join([s for s in curationMountainDiv.splitlines() if s])

print(curationMountainDiv)
