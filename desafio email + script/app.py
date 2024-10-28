import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text
        books.append({'title': title, 'price': price})

    return books

@app.route('/scrape', methods=['GET'])
def scrape():
    books = scrape_books()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
