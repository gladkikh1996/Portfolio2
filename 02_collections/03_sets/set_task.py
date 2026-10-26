##############Задание № 1.1 ########################
europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}
europe_set.add("Исландия")
print(europe_set)
##############Задание № 1.2 ########################
asia_set = {"Япония", "Лаос", "Шри-Ланка", "Китай", "Филиппины", "Камбоджа"}
asia_set.discard("Япония")
print(asia_set)
asia_set.discard("Вьетнам")
print("После discard, ничего не удалит так как во множестве его нет и ошибки не будет, в отличие от remove: ", asia_set)
asia_set.remove("Вьетнам")
print("После remove: ", asia_set)
##############Задание № 1.3 ########################
europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}
europe_set.update({"Испания", "Греция", "Норвегия"})
print(europe_set)
##############Задание № 1.4 ########################
europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}
country_pop = europe_set.pop()
print(country_pop)
##############Задание № 1.5 ########################
new_country = set()
new_country.add("China")
new_country.add("Russia")
new_country.add("Japan")
new_country.add("Singapore")
new_country.add("United Kingdom")
print(new_country)
##############Задание № 1.6 ########################
new_country = {'Singapore', 'China', 'Russia', 'Japan', 'United Kingdom'}
new_country.clear()
print(new_country)
##############Задание № 2.1 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = visited - wishlist
print(result)
###############Задание № 2.2 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = wishlist & visited
print(result)
##############Задание № 2.3 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}
result = european_cities | asian_cities
print(result)
##############Задание № 2.4 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = eco | cheap
print(result)
##############Задание № 2.5 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = winter.issubset(wishlist)
print(result)
##############Задание № 2.6 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = summer | winter
print(result)
##############Задание № 2.7 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

asian_country = "Сеул"
print(asian_country in asian_cities)
##############Задание № 2.8 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = eco & cheap
print(result)
##############Задание № 2.9 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = invited_by_friends - not_interested
print(result)
##############Задание № 2.10 ########################
visited = {"Италия", "Франция"}

wishlist = {"Франция", "Япония", "Норвегия"}


european_cities = {"Париж", "Берлин"}

asian_cities = {"Токио", "Сеул"}


eco = {"Грузия", "Норвегия"}

cheap = {"Грузия", "Армения"}


summer = {"Италия", "Испания"}

winter = {"Норвегия"}


not_interested = {"Вьетнам", "Гренландия"}

invited_by_friends = {"Гренландия", "Исландия"}

result = invited_by_friends >= winter
print(result)