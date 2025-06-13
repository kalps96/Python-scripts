import requests
import pprint

api_url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"

response = requests.get(api_url)

books = response.json()

#for book in books:
    
pprint.pprint(books)