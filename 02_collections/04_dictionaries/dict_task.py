##############Задание № 1.1 ##############
trip = {

"tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},

"plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},

"costs":{"flight":330, "hotel":650, "meals":100, "museums":120}

}
for key in trip["tourist"]:
    if len(key) > 4:
        print(key)
##############Задание № 1.2 ##############
for key in trip["plan"]:
    if key.startswith("F") or key.startswith("G"):
        print(key)
##############Задание № 1.3 ##############
for key, value in trip["tourist"].items():
    if isinstance(value, str) and len(value) > 5:
        print(key, value)
##############Задание № 1.4 ##############
number = 1
for country, city in trip["plan"].items():
    print(f"{number}. Страна: {country}, город: {city}")
    number += 1
##############Задание № 1.5 ##############
sorted_tourist = {}
for key in sorted(trip["tourist"]):
    sorted_tourist[key] = trip["tourist"][key]
print(sorted_tourist)
##############Задание № 1.6 ##############
count = 0
for value in trip["plan"].values():
    if len(value) < 6:
        count += 1
print(count)
##############Задание № 1.7 ##############
for value in trip["plan"].values():
    if "e" in value:
        print(value)
##############Задание № 1.8 ##############
total = 0
for value in trip["costs"].values():
    if value > 100:
        total += value
print(total)
##############Задание № 1.9 ##############
result = []
for key, value in trip["plan"].items():
    if key.startswith("I") or "a" in value:
        result.append(f"{key} -> {value}")
print(result)
##############Задание № 1.10 ##############
for key, value in trip["plan"].items():
    if value == "Rome":
        print(key)
##############Блок № 2##############
##############Задание № 2.1 ##############
trip["tourist"]["email"] = "anna.moreau@example.com"
print(trip["tourist"])
##############Задание № 2.2 ##############
trip["tourist"]["age"] += 1
print(trip["tourist"])
##############Задание № 2.3 ##############
trip["costs"].update({"transport": 60})
print(trip["costs"])
##############Задание № 2.4 ##############
trip["plan"]["Spain"] = "Barcelona"
print(trip["plan"])
##############Задание № 2.5 ##############
museum_clear = trip["costs"].pop("museums")
print("Удален раздел: ", museum_clear)
print(trip["costs"])
##############Задание № 2.6 ##############
trip["plan"].popitem()
print(trip["plan"])
##############Задание № 2.7 ##############
trip["tourist"].clear()
print(bool(trip["tourist"]))
##############Задание № 2.8 ##############
backup_costs = trip["costs"].copy()
backup_costs["hotel"] = 500
print("Оригинал: ", trip["costs"])
print("Копия: ", backup_costs)
##############Задание № 2.9 ##############
trip["tourist"].setdefault("phone", "+7-123-456-7890")
print(trip["tourist"])
##############Задание № 2.10 ##############
del trip["plan"]["France"]
print(trip["plan"])
##############Задание № 2.11 ##############
trip["costs"].update({key: round(value * 1.1, 1) for key, value in trip["costs"].items()})
print(trip["costs"])
##############Задание № 2.12 ##############
trip["plan"] = {key: value for key, value in trip["plan"].items() if value.startswith("D")}
print(trip["plan"])
##############Задание № 2.13 ##############
trip["plan"] = {value: key for key, value in trip["plan"].items()}
print(trip["plan"])
##############Задание № 2.14 ##############
import copy

trip_shallow = copy.copy(trip)
trip_deep = copy.deepcopy(trip)

trip_shallow["costs"]["hotel"] = 700
trip_deep["costs"]["flight"] = 290

print("trip['costs'] =", trip["costs"])
print("trip_shallow['costs'] =", trip_shallow["costs"])
print("trip_deep['costs'] =", trip_deep["costs"])
##############Блок № 3 ##############
##############Задание № 3.1 ##############
cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}
discount_cities = {city: round(price * 0.9, 1) for city, price in cities.items()}
print(discount_cities)
##############Задание № 3.2 ##############
cheap_cities = {}
for city, price in cities.items():
    if price < 200:
        cheap_cities[city] = price
print(cheap_cities)
##############Задание № 3.3 ##############
lower_cities = {}
for city, price in cities.items():
    lower_cities[city.lower()] = price
print(lower_cities)
##############Задание № 3.4 ##############
result = {}
for city in cities:
    length = len(city)
    result.setdefault(length, []).append(city)
print(result)
##############Задание № 3.5 ##############
price_level = {}
for city, price in cities.items():
    if price > 200:
        price_level[city] = "Дорого"
    else:
        price_level[city] = "Приемлемо"
print(price_level)