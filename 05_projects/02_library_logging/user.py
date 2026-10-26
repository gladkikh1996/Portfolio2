"""Функции для работы с пользователями библиотеки."""

from my_logs import logger


MAX_BOOKS_PER_USER = 3

user_books = {}


def borrow_book(username, book):
    """Добавить книгу пользователю с учетом лимита."""
    logger.debug("Пользователь %s пытается взять книгу.", username)

    if book is None:
        logger.warning("Пользователь %s пытается взять недоступную книгу.", username)
        return "Книга недоступна."

    if username not in user_books:
        user_books[username] = []

    if len(user_books[username]) >= MAX_BOOKS_PER_USER:
        logger.warning(
            "Пользователь пытается взять книгу, но достиг лимита: "
            "username=%s, title=%s",
            username,
            book["title"],
        )

        book["available"] = True
        book.pop("borrowed_at", None)

        return f"{username} уже взял максимум книг ({MAX_BOOKS_PER_USER})."

    user_books[username].append(book)

    logger.info(
        "Книга успешно выдана пользователю: username=%s, title=%s",
        username,
        book["title"],
    )

    return f'{username} взял книгу "{book["title"]}".'


def return_book(username, title):
    """Вернуть книгу в библиотеку."""
    logger.debug(
        "Пользователь пытается вернуть книгу: username=%s, title=%s",
        username,
        title,
    )

    if username not in user_books:
        logger.warning(
            "Пользователь пытается вернуть книгу, которой у него нет: "
            "username=%s, title=%s",
            username,
            title,
        )
        return f"{username} не брал книги."

    for book in user_books[username]:
        if book["title"] == title:
            user_books[username].remove(book)
            book["available"] = True

            logger.info(
                "Книга успешно возвращена: username=%s, title=%s",
                username,
                title,
            )

            return f'{username} вернул книгу "{title}".'

    logger.warning(
        "Пользователь пытается вернуть книгу, которой у него нет: "
        "username=%s, title=%s",
        username,
        title,
    )

    return f'{username} не имеет книги "{title}".'


def books_on_hand(username):
    """Информация о книгах у пользователя."""
    books = user_books.get(username, [])
    if not books:
        return f"У {username} нет книг на руках."

    result = f"У {username} на руках {len(books)} книг(и):\n"
    for book in books:
        result += f'- {book["title"]}, взята {book["borrowed_at"]}\n'

    return result
