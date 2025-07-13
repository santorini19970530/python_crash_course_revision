# Python Crash Course, 2Ed, writtern by Eric Matthes

def favourite_book(title):
    print(f"One of my favourite books is {title.title()}.")

books = ['Alice in the Wonderland', 'The Wealth of Nations', '1984']

for book in books:
    favourite_book(book)
