MAX_BOOKS_PER_USER = 3

user_books = {}


def borrow_book(username, book):
    """Добавить книгу пользователю с учетом лимита."""
    if book is None:
        return "Книга недоступна."

    if username not in user_books:
        user_books[username] = []

    if len(user_books[username]) >= MAX_BOOKS_PER_USER:
        return f"{username} уже взял максимум книг ({MAX_BOOKS_PER_USER})."

    user_books[username].append(book)
    return f'{username} взял книгу "{book["title"]}".'


def return_book(username, title):
    """Вернуть книгу в библиотеку."""
    if username not in user_books:
        return f"{username} не брал книги."

    for book in user_books[username]:
        if book["title"] == title:
            user_books[username].remove(book)
            book["available"] = True
            return f'{username} вернул книгу "{title}".'

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
