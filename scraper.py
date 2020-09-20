import requests
import pprint
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def hn_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'])

def create_new_hn_site(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    #return len(hn)
    return hn_stories_by_votes(hn)

pprint.pprint(create_new_hn_site(links, subtext))
#create_new_hn_site(links, subtext)
