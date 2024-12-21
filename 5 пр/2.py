import requests
import json
import random

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year} ({self.genre})"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
        else:
            print(f"{self.name} уже взял книгу '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} не брал книгу '{book.title}'.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"{self.name} (ID: {self.reader_id}) - Взятые книги: {', '.join(borrowed_titles) if borrowed_titles else 'нет книг'}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Книга '{book.title}' добавлена в библиотеку.")
        else:
            print(f"Книга '{book.title}' уже существует в библиотеке.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Книга '{book.title}' удалена из библиотеки.")
        else:
            print(f"Книга '{book.title}' не найдена в библиотеке.")

    def register_reader(self, reader):
        if reader not in self.readers:
            self.readers.append(reader)
            print(f"Читатель '{reader.name}' зарегистрирован.")
        else:
            print(f"Читатель '{reader.name}' уже зарегистрирован.")

    def lend_book(self, reader, book):
        if book in self.books:
            if reader in self.readers:
                reader.borrow_book(book)
                self.remove_book(book)
                print(f"Книга '{book.title}' выдана читателю '{reader.name}'.")
            else:
                print(f"Читатель '{reader.name}' не зарегистрирован.")
        else:
            print(f"Книга '{book.title}' не доступна в библиотеке.")

    def return_book(self, reader, book):
        if reader in self.readers:
            reader.return_book(book)
            self.add_book(book)
            print(f"Книга '{book.title}' возвращена читателем '{reader.name}'.")
        else:
            print(f"Читатель '{reader.name}' не зарегистрирован.")

    def find_book(self, title=None, author=None):
        found_books = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or (author and author.lower() in book.author.lower()):
                found_books.append(book)
        return found_books

    def get_reader_books(self, reader):
        if reader in self.readers:
            return reader.borrowed_books
        else:
            print(f"Читатель '{reader.name}' не зарегистрирован.")
            return []

def main():
    library = Library("Городская библиотека")

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Зарегистрировать читателя")
        print("4. Выдать книгу")
        print("5. Вернуть книгу")
        print("6. Найти книгу")
        print("7. Показать книги читателя")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            genre = input("Введите жанр книги: ")
            book = Book(title, author, year, genre)
            library.add_book(book)

        elif choice == '2':
            title = input("Введите название книги для удаления: ")
            found_books = library.find_book(title=title)
            if found_books:
                library.remove_book(found_books[0]) 
            else:
                print(f"Книга '{title}' не найдена.")

        elif choice == '3':
            name = input("Введите имя читателя: ")
            reader_id = input("Введите ID читателя: ")
            reader = Reader(name, reader_id)
            library.register_reader(reader)

        elif choice == '4':
            reader_name = input("Введите имя читателя: ")
            title = input("Введите название книги для выдачи: ")
            found_books = library.find_book(title=title)
            reader = next((r for r in library.readers if r.name == reader_name), None)
            if found_books and reader:
                library.lend_book(reader, found_books[0])  
            else:
                if not reader:
                    print(f"Читатель '{reader_name}' не зарегистрирован.")
                else:
                    print(f"Книга '{title}' не найдена.")

        elif choice == '5':
            reader_name = input("Введите имя читателя: ")
            title = input("Введите название книги для возврата: ")
            found_books = library.find_book(title=title)
            reader = next((r for r in library.readers if r.name == reader_name), None)
            if found_books and reader:
                library.return_book(reader, found_books[0]) 
            else:
                if not reader:
                    print(f"Читатель '{reader_name}' не зарегистрирован.")
                else:
                    print(f"Книга '{title}' не найдена.")

        elif choice == '6':
            title = input("Введите название книги для поиска: ")
            found_books = library.find_book(title=title)
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(book)
            else:
                print(f"Книги с названием '{title}' не найдены.")

        elif choice == '7':
            reader_name = input("Введите имя читателя: ")
            reader = next((r for r in library.readers if r.name == reader_name), None)
            if reader:
                borrowed_books = reader.borrowed_books
                if borrowed_books:
                    print(f"Книги, взятые читателем '{reader_name}':")
                    for book in borrowed_books:
                        print(book)
                else:
                    print(f"Читатель '{reader_name}' не взял ни одной книги.")
            else:
                print(f"Читатель '{reader_name}' не зарегистрирован.")

        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Ошибка: неверный ввод. Пожалуйста, выберите действие от 1 до 8.")

if __name__ == "__main__":
    main()