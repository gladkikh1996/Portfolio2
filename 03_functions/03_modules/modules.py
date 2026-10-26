countries = ['Италия', 'Франция', 'Япония', 'Норвегия', 'Чили', 'Канада', 'Перу']
companions = ['Анна', 'Олег', 'Ирина', 'Михаил', 'Светлана']
places = ['Эйфелева башня', 'Колизей', 'Фудзи', 'Биг-Бен', 'Ниагарский водопад']

###########Задание № 1.1################
import random
country = random.choice(countries)
print(country)
###########Задание № 1.2################
day = random.randint(1, 31)
print(day)
###########Задание № 1.3################
rate = round(random.uniform(0.90, 0.95), 2)
print("1.3 Курс обмена валют:", rate)

###########Задание № 1.4################
flight_number = random.randint(1000, 9999)
print("1.4 Номер рейса:", flight_number)

###########Задание № 1.5################
selected_places = random.choices(places, k=3)
print("1.5 Достопримечательности с повторами:", selected_places)

###########Задание № 1.6################
trip_countries = random.sample(countries, 3)
print("1.6 Три разные страны:", trip_countries)

###########Задание № 1.7################
discount = random.randint(5, 30)
print("1.7 Скидка на билет:", discount, "%")

###########Задание № 1.8################
visa_chance = random.randint(1, 100)
print("1.8 Шанс визы:", visa_chance, "%")
if visa_chance >= 70:
    print("Виза одобрена")
else:
    print("Виза отклонена")

###########Задание № 1.9################
companion = random.choice(companions)
print("1.9 Случайный попутчик:", companion)

###########Задание № 1.10################
budget = round(random.uniform(800, 2000), 2)
print("1.10 Бюджет поездки:", budget, "евро")

#######################БЛОК № 2########################
###########Задание № 2.1################
from datetime import datetime

book_datetime = datetime.strptime("24-03-2026", "%d-%m-%Y")
print(book_datetime)
###########Задание № 2.2################
from datetime import datetime

book_date = datetime.strptime("10-04-1925", "%d-%m-%Y")
today = datetime.today()

years = today.year - book_date.year - ((today.month, today.day) < (book_date.month, book_date.day))

print(years)
###########Задание № 2.3################
from datetime import date, timedelta

start_date = date.today()
end_date = start_date + timedelta(days=14)

print(end_date)
###########Задание № 2.4################
from datetime import time

book_time = time(21, 30)
print(book_time)
###########Задание № 2.5################
from datetime import date

today = date.today()
formatted_date = today.strftime("%d.%m.%Y")

print(formatted_date)
###########Задание № 2.6################
book1_year = 2005
book2_year = 2015

if book1_year > book2_year:
    print("Первая книга новее")
elif book2_year > book1_year:
    print("Вторая книга новее")
else:
    print("Книги одного года издания")
###########Задание № 2.7################
from datetime import date

publish_date = date(2010, 5, 5)
print(publish_date)
###########Задание № 2.8################
from datetime import datetime

review_datetime = datetime(2021, 2, 14, 18, 45)
print(review_datetime)
###########Задание № 2.9################
from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_now)
###########Задание № 2.10################
from datetime import date

today = date.today()

day_number = today.day
days_passed = today.day - 1

print("Номер дня месяца:", day_number)
print("Прошло дней с начала месяца:", days_passed)
###########Блок № 3################
###########Задание № 3.1################
import math

width = 16
height = 9

diagonal = math.sqrt(width ** 2 + height ** 2)
print(round(diagonal, 2))
###########Задание № 3.2################
import math

seats = 267
row_size = 20

full_rows = seats // row_size
print(full_rows)
###########Задание № 3.3################
import math

films = 3
minutes_per_film = 12

total_minutes = films * minutes_per_film
total_hours = total_minutes / 60

result = math.ceil(total_hours)
print(result)
###########Задание № 3.4################
import math

diameter = 4
circle_length = math.pi * diameter

print(round(circle_length, 2))
###########Задание № 3.5################
import math

t = 2
interest = 100 * math.exp(-0.3 * t)

print(round(interest, 2))
###########Задание № 3.6################
import math

ways = math.factorial(5)
print(ways)
###########Задание № 3.7################
import math

d = 3.5
light = 1000 / (d ** 2)

print(round(light, 2))
###########Задание № 3.8################
import math

tickets = 50
per_time = 7

times = math.ceil(tickets / per_time)
print(times)
###########Задание № 3.9################
import math

minutes = 113
full_hours = math.floor(minutes / 60)

print(full_hours)
###########Задание № 3.10################
import math

movie_duration = 137
interval = 30

next_session = math.ceil(movie_duration / interval) * interval
print(next_session)
###########Блок № 4################
###########Задание № 4.1################
import json

book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genres": ["dystopia", "political fiction", "science fiction"],
    "pages": 328,
    "available": True,
    "rating": 4.7
}

book_json = json.dumps(book)
print(book_json)
###########Задание № 4.2################
import json

data = '''
[
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genres": ["dystopia", "political fiction"]
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "genres": ["dystopia", "science fiction"]
    },
    {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "year": 1953,
        "genres": ["dystopia", "speculative fiction"]
    }
]
'''

books = json.loads(data)
print(books[0]["author"])
###########Задание № 4.3################
import json

library = {
    "library_name": "Central Library",
    "location": "Main Street, 10",
    "books": [
        {"title": "1984", "author": "George Orwell", "available": True},
        {"title": "Brave New World", "author": "Aldous Huxley", "available": False},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury", "available": True}
    ]
}

library_json = json.dumps(library)
print(library_json)
###########Задание № 4.4################
import json

json_data = '''
[
    {"title": "1984", "author": "George Orwell", "available": true},
    {"title": "Brave New World", "author": "Aldous Huxley", "available": false},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "available": true}
]
'''

books = json.loads(json_data)

available_titles = []

for book in books:
    if book["available"] == True:
        available_titles.append(book["title"])

print(available_titles)