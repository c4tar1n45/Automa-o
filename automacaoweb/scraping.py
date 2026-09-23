import requests
from bs4 import BeautifulSoup
import sys
import io
import time
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://books.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:

    # Título

    title = book.h3.a['title']


     # Preço

    price = book.find('p', class_='price_color').text


    # Classificação

    rating = book.p['class'][1]  # A segunda classe indica a classificação por estrelas

    print(f'Título: {title}')

    print(f'Preço: {price}')

    print(f'Classificação: {rating}')

    print('-' * 40)

# Navegação em múltiplas páginas

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'


for page in range(1, 51):  # O site possui 50 páginas

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:

        title = book.h3.a['title']

        price = book.find('p', class_='price_color').text

        rating = book.p['class'][1]

        print(f'Título: {title}')

        print(f'Preço: {price}')

        print(f'Classificação: {rating}')

        print('-' * 40)


    time.sleep(1)  # Pausa de 1 segundo entre as requisições

# Salvando os dados em CSV

with open('books.csv', 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)

    writer.writerow(['Título', 'Preço', 'Classificação'])

    for page in range(1, 51):

        url = base_url.format(page)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('article', class_='product_pod')

        for book in books:

            title = book.h3.a['title']

            price = book.find('p', class_='price_color').text

            rating = book.p['class'][1]

            writer.writerow([title, price, rating])

        time.sleep(1)