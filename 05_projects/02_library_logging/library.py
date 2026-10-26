"""Функции для работы с библиотекой."""

import json
from datetime import datetime
from pathlib import Path

from my_logs import logger


library_books = []  # Список всех книг


def load_books_from_file():
    """Загрузить книги из JSON файла."""
    path = Path("data/books.json")

    logger.debug("Начинаю загрузку книг из файла %s", path)

    if not path.exists():
        logger.critical(
            "Файл %s не найден. Библиотека не может стартовать корректно.",
            path,
        )
        return "Файл с книгами не найден."

    try:
        with path.open("r", encoding="utf-8") as file:
            books_data = json.load(file)

        if not isinstance(books_data, list):
            logger.error("Неверный формат файла %s. Ожидался список книг.", path)
            return "Ошибка: неверный формат файла с книгами."

    except json.JSONDecodeError as error:
        logger.error("JSONDecodeError при чтении файла %s: %s", path, error)
        return "Ошибка: не удалось прочитать JSON."

    loaded_books_count = 0

    for book in books_data:
        logger.debug("Обрабатываю запись книги из .json: %s", book)

        if not isinstance(book, dict):
            logger.warning("Пропущена запись книги не в формате словаря: %s", book)
            continue

        title = book.get("title")
        author = book.get("author")

        if not title or not author:
            logger.warning("Пропущена запись без title/author: %s", book)
            continue

        library_books.append(
            {
                "title": title,
                "author": author,
                "available": True,
            }
        )
        loaded_books_count += 1

        logger.info(
            "Книга успешно добавлена в библиотеку: title=%s, author=%s",
            title,
            author,
        )

    logger.debug("Загрузка книг завершена. Загружено книг: %s", loaded_books_count)

    return f"Загружено {loaded_books_count} книг(и) из файла."


def add_book(title, author):
    """Добавить книгу в библиотеку."""
    book = {"title": title, "author": author, "available": True}
    library_books.append(book)

    logger.info(
        "Книга успешно добавлена в библиотеку: title=%s, author=%s",
        title,
        author,
    )

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
    logger.debug("Ищу книгу для выдачи: %s", title)

    for book in library_books:
        logger.debug("Проверяю книгу: %s", book["title"])

        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            book["borrowed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

            logger.debug("Книга найдена и подготовлена к выдаче: %s", title)

            return book

    logger.debug("Книга не найдена или уже недоступна: %s", title)

    return None
