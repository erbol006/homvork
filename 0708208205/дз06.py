class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Непрочитана"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Книги с таким названием не найдены.")

    def find_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Книги этого автора не найдены.")

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Книга '{title}' отмечена как прочитанная.")
                return
        print("Книга не найдена.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{title}' удалена из библиотеки.")
                return
        print("Книга не найдена.")

    def filter_books(self, read_status):
        filtered_books = [book for book in self.books if book.read == read_status]
        if filtered_books:
            for book in filtered_books:
                print(book)
        else:
            print("Книги с заданным статусом не найдены.")

    def sort_books_by_year(self):
        self.books.sort(key=lambda book: book.year)
        print("Книги отсортированы по году публикации.")


def main():
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Просмотреть список книг")
        print("3. Найти книгу по названию")
        print("4. Найти книгу по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Удалить книгу")
        print("7. Фильтровать книги по статусу")
        print("8. Отсортировать книги по году публикации")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год публикации: "))
            library.add_book(Book(title, author, year))
            print(f"Книга '{title}' добавлена в библиотеку.")

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            title = input("Введите название книги для поиска: ")
            library.find_by_title(title)

        elif choice == '4':
            author = input("Введите автора для поиска: ")
            library.find_by_author(author)

        elif choice == '5':
            title = input("Введите название книги, которую хотите отметить как прочитанную: ")
            library.mark_book_as_read(title)

        elif choice == '6':
            title = input("Введите название книги для удаления: ")
            library.remove_book(title)

        elif choice == '7':
            status = input("Введите статус (прочитанные/непрочитанные): ").strip().lower()
            if status == "прочитанные":
                library.filter_books(read_status=True)
            elif status == "непрочитанные":
                library.filter_books(read_status=False)
            else:
                print("Неверный статус.")

        elif choice == '8':
            library.sort_books_by_year()
            library.list_books()

        elif choice == '9':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
