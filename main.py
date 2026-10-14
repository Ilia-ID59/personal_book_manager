name = input("type your name : ")
print("welcome", name)

books = []
count = int(input("how mane book do you want in list ? "))
for b in range(count):
    name_book = input("whats your name book ? ")
    books.append(name_book)

print("your books:")
for name_book in books:
    print(name_book)