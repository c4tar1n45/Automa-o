import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://www.google.com.br'
resposta = requests.get(url)

html = '''
    <html>
        <body>
            <h1>Olá Mundo</h1>
            <p>Bem-Vindo</p>
        </body>
    <html>

'''
soup = BeautifulSoup(html, 'html.parser')

print(soup.p.text)
