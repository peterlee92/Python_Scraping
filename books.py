from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('./csv/books.csv', mode='w',encoding='utf8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'year', 'genre', 'ratings', 'ages', 'description', 'author', 'illustrator', 'img', 'url'])

source = requests.get('https://www.commonsensemedia.org/lists/50-books-all-kids-should-read-before-theyre-12').text
soup = BeautifulSoup(source, 'lxml')

booksDiv = soup.find('div', class_='view-content')
srcs = booksDiv.find_all('div', class_='review-product-image')
srcList = []

for src in srcs :
    srcList.append(src.a['href'])

for book in srcList:
    source = requests.get('https://www.commonsensemedia.org'+book).text
    soup = BeautifulSoup(source, 'lxml')

    title = (soup.find('h1')).text

    yearDiv = soup.find('div', class_='item-list')
    year = (yearDiv.find('li', class_='last')).text

    genreDiv = soup.find('div', class_='shutter-summary-pane panel-pane pane-product-details')
    genre = (genreDiv.find('li', class_='types')).a.text

    ratingsClass = soup.find('div', class_='ratings-small')['class']
    ratings = int(ratingsClass[2].split('-')[1])*2

    ages = ((soup.find('div', class_='csm-green-age')).text).split(' ')[1]

    description = (soup.find('div', class_='pane-node-field-what-is-story')).p.text

    detailDiv = soup.find('div', class_='pane-product-details')
    author = detailDiv.find('li',class_='0').a.text

    illustrator = detailDiv.find('li', class_='1').a.text

    img = soup.find('div', class_='pane-node-field-product-image').img['src']

    url = ''

    csv_writer.writerow([title, year, genre, ratings, ages, description, author, illustrator, img, url])

# source = requests.get('https://www.commonsensemedia.org/book-reviews/dont-let-the-pigeon-drive-the-bus').text
# soup = BeautifulSoup(source, 'lxml')

# title = (soup.find('h1')).text
# # print(title)

# yearDiv = soup.find('div', class_='item-list')
# year = (yearDiv.find('li', class_='last')).text
# # print(year)

# genreDiv = soup.find('div', class_='shutter-summary-pane panel-pane pane-product-details')
# genre = (genreDiv.find('li', class_='types')).a.text
# # print(genre)

# ratingsClass = soup.find('div', class_='ratings-small')['class']
# ratings = int(ratingsClass[2].split('-')[1])*2
# # print(ratings)

# ages = ((soup.find('div', class_='csm-green-age')).text).split(' ')[1]
# # print(ages)

# description = (soup.find('div', class_='pane-node-field-what-is-story')).p.text
# # print(description)

# detailDiv = soup.find('div', class_='pane-product-details')
# author = detailDiv.find('li',class_='0').a.text
# # print(author)

# illustrator = detailDiv.find('li', class_='1').a.text
# # print(illustrator)

# img = soup.find('div', class_='pane-node-field-product-image').img['src']
# # print(img)
