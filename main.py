from books import show_books

name = input("type your name : ")
print("welcome", name)

books = []
count = int(input("how mane book do you want in list ? "))

for b in range(count):
    name_book = input("whats your name book ? ")
    books.append(name_book)

show_books(books)
    