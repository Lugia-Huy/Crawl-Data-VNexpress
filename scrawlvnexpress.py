import bs4 as bs
import urllib.request
import csv
import random
__all__ = [bs, urllib.request, csv]

baseURL = 'https://vnexpress.net/'
CATEGORIES = [  
    'giao-duc',
    'suc-khoe',
    'khoa-hoc',
    'so-hoa',
    'giai-tri',
    'the-thao',
    'doi-song',
    'du-lich'
]

TOPICS = {
    'giao-duc': 'Giáo dục',
    'suc-khoe': 'Sức khoẻ - Y tế',
    'khoa-hoc': 'Khoa học',
    'so-hoa': 'Công nghệ',
    'giai-tri': 'Giải trí',
    'the-thao': 'Thể thao',
    'doi-song': 'Đời sống',
    'du-lich': 'Du lịch'
}

DATA = random.sample(CATEGORIES, 8)
for topic in DATA: 
    url = urllib.request.urlopen(baseURL+topic).read()
    soup = bs.BeautifulSoup(url, 'lxml')
    pages = soup.find_all('p', class_="description")

    for page in pages:
        titles = page.find('a').attrs['title']
        links = page.find('a').attrs['href']
        print('Title: {} - Link: {}'.format(titles, links))

    with open(TOPICS[topic]+'.csv', 'w', encoding='utf-16') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Link', 'Topic'])

        for page in pages:
            titles = page.find('a').attrs['title']
            links = page.find('a').attrs['href']
            writer.writerow([titles,  links, TOPICS[topic]])
