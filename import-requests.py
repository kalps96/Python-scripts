
import requests
import pprint

api_url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"

response = requests.get(api_url)

books = response.json()

#pprint.pprint(books)
def unknown_list_author (book):
    return book.get("country", "") == "United States"
b = filter(unknown_list_author, books)
filtered_books = list(b)


pprint.pprint(filtered_books)

print("count:", len(filtered_books))