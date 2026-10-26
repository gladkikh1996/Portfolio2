import json
from datetime import datetime
from pathlib import Path

library_books = []  # Список всех книг


def load_books_from_file():
    """Загрузить книги из JSON файла."""
    path = Path("data/books.json")
    if not path.exists():
        return "Файл с книгами не найден."

    try:
        with open(path, "r", encoding="utf-8") as file:
            books_data = json.load(file)
        if not isinstance(books_data, list):
            return "Ошибка: неверный формат файла с книгами."
    except json.JSONDecodeError:
        return "Ошибка: не удалось прочитать JSON."

    for book in books_data:
        title = book.get("title")
        author = book.get("author")
        if not title or not author:
            continue

        library_books.append(
            {
                "title": title,
                "author": author,
                "available": True,
            }
        )

    return f"Загружено {len(books_data)} книг(и) из файла."


def add_book(title, author):
    """Добавить книгу в библиотеку."""
    book = {"title": title, "author": author, "available": True}
    library_books.append(book)
    return f'Книга "{title}" добавлена в библиотеку.'


def list_books():
    """Вывести список всех книг."""
    if not library_books:
        return "В библиотеке пока нет книг."

    result = "Список книг:\n"
    for book in library_books:
        status = "Доступна" if book["available"] else "Выдана"
        result += f'- {book["title"]} ({book["author"]}) — {status}\n'

    return result


def checkout_book(title):
    """Выдать книгу пользователю."""
    for book in library_books:
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            book["borrowed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            return book

    return None
