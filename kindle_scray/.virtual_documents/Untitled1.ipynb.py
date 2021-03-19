import requests


url = "https://en.wikipedia.org/w/index.php" + \
    "?title=List_of_Game_of_Thromes_episodes&oldid=802553687"


r = requests.get(url)


html_contents = r.text


from bs4 import BeautifulSoup


html_soup = BeautifulSoup(html_contents)


html_contents.find('h1')


html_soup.find('h1')


html_soup.find('',{'id':'p-logo'})


for found in html_soup.find_all((['h1','h2'])):
    print(found)


first_h1 = html_soup.find('h1')


first_h1


first_h1.name


first_h1.contents


first_h1


first_h1.text


first_h1.get_text()


first_h1.attrs['id']


first_h1['id']


first_h1.get('id')


cites = html_soup.find_all('cite', class_='citation', limit=5)


for citation in cites:
    link = citation.find('a')
    print(link.get('href'))
    print()


episodes = []

ep_tables = html_soup.find_all('table', class_='wikiepisodetable')


for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    for header in table.find_all('tr').find_all('th'):
        headers.append(header.text)
        
        


html_soup.select('a')



