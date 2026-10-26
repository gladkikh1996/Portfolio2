from library import checkout_book, list_books, load_books_from_file
from user import books_on_hand, borrow_book, return_book
from utils import greet, print_separator

# Приветствие
greet()
print_separator()

# Загружаем книги из JSON
print(load_books_from_file())
print_separator()

# Выдаём книгу Ане
book = checkout_book("1984")
print(borrow_book("Аня", book))
print(books_on_hand("Аня"))

print_separator()

# Выдаём книгу Диме
book = checkout_book("Портрет Дориана Грея")
print(borrow_book("Дима", book))
print(books_on_hand("Дима"))

# Выдаём книгу Диме
book = checkout_book("Три товарища")
print(borrow_book("Дима", book))
print(books_on_hand("Дима"))

# Выдаём книгу Диме
book = checkout_book("Анна Каренина")
print(borrow_book("Дима", book))
print(books_on_hand("Дима"))

# Выдаём книгу Диме
book = checkout_book("О дивный новый мир")
print(borrow_book("Дима", book))
print(books_on_hand("Дима"))

print_separator()

# Возврат книги Ани
print(return_book("Аня", "1984"))
print(books_on_hand("Аня"))
print_separator()

# Возврат книги Димы
print(return_book("Дима", "Атлант расправил плечи"))
print(books_on_hand("Аня"))
print_separator()

# Список книг после возврата
print(list_books())
