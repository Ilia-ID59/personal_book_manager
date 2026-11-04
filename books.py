import json 

def show_books(books):
    for name_book in books:
        print(name_book["name"], " -  priority : ", name_book["priority"])

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file_books:
        json.dump(books, file_books, ensure_ascii=False, indent=2)

def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file_books:        
            return json.load(file_books)
        
    except FileNotFoundError:
        return []    
    