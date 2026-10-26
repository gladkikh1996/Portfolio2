books = [
    "Гордость и предубеждение",
    "Мастер и Маргарита",
    "Три товарища",
    "Сто лет одиночества",
    "Унесённые ветром",
    "Тень горы",
    "Цветы для Элджернона",
    "О дивный новый мир",
    "Норвежский лес",
    "Имя розы",
]

catalog = {
    "Джейн Остин": "Гордость и предубеждение",
    "Михаил Булгаков": "Мастер и Маргарита",
    "Эрих Мария Ремарк": "Три товарища",
    "Габриэль Гарсиа Маркес": "Сто лет одиночества",
    "Умберто Эко": "Имя розы",
}


total_pages = 1200
days = 0

############Задание № 1.1#############
def task_1(total_pages, days):
    try:
        pages_per_day = total_pages // days
        print(f"Страниц в день: {pages_per_day}")
    except ZeroDivisionError:
        print("Ошибка: на ноль делить нельзя")
    finally:
        print("Расчёт завершён")


task_1(total_pages, days)
task_1(total_pages, 10)
############Задание № 1.2#############
def task_2(books, ind):
    try:
        book = books[ind]
    except IndexError:
        print("Ошибка: книги с таким индексом нет")
    else:
        print(f"Книга найдена: {book}")
    finally:
        print("Работа со списком завершена")


task_2(books, 15)
task_2(books, 5)
############Задание № 1.3############
def task_3(books, ind):
    try:
        num = int(books[ind])
        print(f"Получилось число: {num}")
    except ValueError:
        print("Ошибка: название книги нельзя преобразовать в число")


task_3(books, 0)
############Задание № 1.4############
def task_4(books, days):
    try:
        result = books + days
        print(f"Результат: {result}")
    except TypeError:
        print("Ошибка: нельзя сложить список и число")
    finally:
        print("Получение суммы завершено")


task_4(books, days)
############Задание № 1.5############
def task_5(catalog, author):
    try:
        book = catalog[author]
    except KeyError:
        print("Ошибка: такого автора нет в каталоге")
    else:
        print(f"Найдена книга: {book}")
    finally:
        print("Поиск завершён")


task_5(catalog, "Михаил Булгаков")
task_5(catalog, "Сергей Довлатов")
############Задание № 1.6############
def task_6():
    try:
        print(penalty_rate)
    except NameError:
        print("Ошибка: переменная penalty_rate не существует")

task_6()
############Задание № 1.7############
def task_7():
    try:
        import recommendations_engine
    except ModuleNotFoundError:
        print("Ошибка: модуль recommendations_engine не найден")

task_7()
############Задание № 1.8############
def task_8(books, book_idx_str, mult):
    try:
        book_idx = int(book_idx_str)

        if not isinstance(mult, (int, float)):
            raise TypeError("mult должен быть числом")

        book = books[book_idx]
        result = book_idx * mult

    except (ValueError, IndexError, TypeError) as error:
        print(f"Ошибка: {type(error).__name__}")
    else:
        print(f"Книга найдена: {book}")
        print(f"Произведение: {result}")
    finally:
        print("Работа функции завершена")

task_8(books, "2", 3)
task_8(books, "три", 3)
task_8(books, "5", "4")
task_8(books, "5", None)

