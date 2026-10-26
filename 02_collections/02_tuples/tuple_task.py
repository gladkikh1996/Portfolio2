#############Задание № 1.1 #################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
for i, city in enumerate(cities):
    print(i, city)
############Задание № 1.2 ##################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
for i in range(len(cities)):
    print(i, cities[i])
##########Задание № 1.3 #################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
print(cities[::-1])
############Задание № 1.4##############
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
for i in cities[1:-1]:
    print(i)
########Задание № 1.5################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва",)
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
for i in cities[1::2]:
    print(i)
##########Задание № 1.6################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
for i in landmarks:
    if i.startswith("Б"):
        print(i)
###############Задание № 1.7############
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
start_index = cities.index("Берлин")
print(start_index)
print(cities[2:5])
##############Задание № 1.8############
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
dyble_cities = ()
for city in cities:
    dyble_cities = dyble_cities + (city, city)
print(dyble_cities)
##########Задание № 1.9 ###################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
for city in cities[:3]:
    print(city + "!")
##########Задание № 1.10 ###################
cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
print("id до изменений: ", id(cities))
cities = (*cities, "Серпухов", "Чехов")
print("id после изменений", id(cities))
print(cities)
#########Задание № 2.1 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
uniq_city = set(visited)
for city in uniq_city:
    result = visited.count(city)
    print(f"{city}: {result}")
#########Задание № 2.2 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
print(visited.index("Вена"))
#########Задание № 2.3 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
if "Амстердам" in visited:
    print("Турист был в Амстердаме")
else:
    print("Турист не был в Амстердаме")
#########Задание № 2.4 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
k = 0
city = ""
for item in set(visited):
    count_city = visited.count(item)
    if count_city > k:
        k = count_city
        city = item
print(f"Турист чаще всего был в городе {city}: {k}")
#########Задание № 2.5 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
for city in visited:
    if visited.count(city) == 1:
        print(city)
#########Задание № 2.6 #############
countries = ("Франция", "Италия", "Франция", "Австрия", "Германия", "Германия")
print(len(set(countries)))
##########Задание № 2.7 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
for i in range(len(visited)):
    if visited[i] == "Париж":
        print(i)
#########Задание № 2.8 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
rome_count = visited.count("Рим")
vena_count = visited.count("Вена")
if rome_count < vena_count:
    print("Посещений больше у Вены")
elif rome_count > vena_count:
    print("Посещений больше у Рима")
else:
    print("Одинаковое посещение у Рима и Вены")
#########Задание № 2.9 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
for city in set(visited):
    city_count = visited.count(city)
    if city_count >= 2:
        print(f"Город: {city}: {city_count}")
#########Задание № 2.10 #############
visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
part = visited[2:5]
idx = part.index("Вена")
result = idx + 2
print(result)
##########Задание № 2.11 #############
eurotrip = ("Минск", "Варшава", "Будапешт", ["Загреб", "Зальцбург", "Вена"], "Мюнхен")
print(eurotrip)
print("Выведен кортеж с номером id: ", id(eurotrip))
eurotrip[3].remove("Зальцбург")
eurotrip[3].append("Любляна")
print("После изменений: ", eurotrip)
print("Выведен кортеж с новым номером id: ", id(eurotrip))
