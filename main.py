from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("type your name : ")
print("welcome", name)

admin_mode = input("do you want to enter admin mode ? (yes/no) ")
if admin_mode == "yes":
    admin_password = input("enter admin password : ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated ")
    else:
        print("wrong password ")


books = load_books()
count_book = int(input("how mane book do you want in list ? "))

for b in range(count_book):
    name_book = input("whats your name book ? ")
    priority = input("enter priority (low / medium / high) : ").lower()

    book = {
        "name" : name_book,
        "priority" : priority
    }
    books.append(book)

show_books(books)
save_books(books)
