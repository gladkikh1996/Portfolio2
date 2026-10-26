##############№ 1.1####################
def cooking_decorated(func):
    def wrapper(meal):
        print(f"Готовим: {meal}")
        func(meal)
    return wrapper

@cooking_decorated
def cook(meal):
    print(f"{meal} готово")

cook("Борщ")
##############№ 1.2####################
def repeat (func):
    def wrapper(n, meal):
        for i in range(1, n + 1):
            print(f"{meal}: порция {i}")
        func(n, meal)
    return wrapper

@repeat
def serve(n, meal):
    print(f"{meal} подано")

serve(3, "Пицца")
##############№ 1.3####################
def log_ingredients(func):
    def wrapper(meal, **ingredients):
        for name, ingredient in ingredients.items():
            print(f"{name}: {ingredient}")
        func(meal, **ingredients)
    return wrapper

@log_ingredients
def cook_meal(meal, **ingredients):
    print(f"{meal} готово")

cook_meal("Греческий салат", томаты="2 шт", огурцы="1 шт", сыр="100 г", масло="1 ст.л")
##############№ 1.4####################
def validate_positive(func):
    def wrapper(minutes, grams_meat):
        if minutes > 0 and grams_meat > 0:
            func(minutes, grams_meat)
        else:
            print("Неверные данные")
    return wrapper


@validate_positive
def marinate(minutes, grams_meat):
    print(f"Мариновать {grams_meat} г мяса {minutes} мин.")


marinate(30, 500)
marinate(0, 500)
##############№ 1.5####################
def total_cost_decorator(func):
    def wrapper(*prices):
        total = sum(prices)
        print(f"Общая стоимость: {total}")
        func(*prices)
    return wrapper


@total_cost_decorator
def count_ingredients(*prices):
    print(f"Куплено ингредиентов: {len(prices)}")


count_ingredients(100, 50, 70, 30)
##############Блок № 2####################
##############№ 2.1####################
def filter_cinema(func):
    def wrapper(film_ratings, min_rating):
        filtered_films = []

        for film, rating in film_ratings.items():
            if rating >= min_rating:
                filtered_films.append(film)

        func(filtered_films)
    return wrapper

@filter_cinema
def show_films(films):
    print(f"Отфильтрованные фильмы: {films}")

film_ratings = {
    "Дюна": 9,
    "Матрица": 10,
    "Начало": 7,
    "Крёстный отец": 9,
    "Ёлки 5": 5
}

show_films(film_ratings, 8)

##############№ 2.2####################
def time_duration(func):
    def wrapper(durations):
        total_time = sum(durations.values())
        count_films = len(durations)
        average = total_time / count_films
        print(f"Средняя длительность фильмов: {average}")
        func(durations)
    return wrapper

@time_duration
def show_duration_info(durations):
    print("Длительность фильмов посчитана")

durations = {
    "Дюна": 155,
    "Матрица": 136,
    "Начало": 148
}

show_duration_info(durations)
##############№ 2.3####################
import random

def my_decorate (func):
    def wrapper(*prices):
        total = sum(prices)
        discount = random.randint(1, 50)
        final_price = total - discount

        print(f"Скидка: {discount} руб, Итого: {final_price} руб")
        func(*prices)
    return wrapper

@my_decorate
def count_snacks(*prices):
    print(f"Количество купленных закусок: {len(prices)}")

count_snacks(120, 80, 60, 140)
##############№ 2.4####################
def time_true (func):
    def wrapper(film, time):
        if 8 <= time <= 23:
            func(film, time)
        else:
            print("Сеанс вне допустимого диапазона")
    return wrapper

@time_true
def show_session(film, time):
    print(f"Фильм: {film}, начало в {time}:00")

show_session("Интерстеллар", 2)
show_session("Дюна", 19)
##############№ 2.5####################
def check_film (func):
    def wrapper(film, schedule):
        if film in schedule:
            func(film, schedule)
        else:
            print("Фильма нет в расписании")
    return wrapper

@check_film
def show_film_time(film, schedule):
    print(f"Фильм: {film}, начало в {schedule[film]}")

schedule = {
    "Дюна": "18:00",
    "Матрица": "20:30",
    "Интерстеллар": "23:00",
    "Шрек 2": "16:20"
}

show_film_time("Аватар", schedule)
show_film_time("Матрица", schedule)

