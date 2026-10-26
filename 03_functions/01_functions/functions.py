#####################Задание № 1.1#################
def daily_reminder():
    print("Не забудь выпить воду и сделать растяжку сегодня!")

daily_reminder()
#####################Задание № 1.2#################
def log_sleep(hours):
    print("Сегодня вы поспали", hours, "часов")
log_sleep(5)
#####################Задание № 1.3#################
def calculate_water_intake(weight, age):
    if age < 30:
        water_ml = weight * 40
    elif age <= 55:
        water_ml = weight * 35
    else:
        water_ml = weight * 30

    water_litr = water_ml / 1000
    return water_litr

print(calculate_water_intake(70, 25))
print(calculate_water_intake(70, 40))
print(calculate_water_intake(70, 60))
#####################Задание № 1.4#################
def track_mood(mood="Хорошее", energy=7):
    print("Ваше настроение: ", mood)
    print("Уровень энергии: ", energy)
track_mood("Отличное", 9)
track_mood()
#####################Задание № 1.5#################
def list_healthy_habits(*privuchki):
    print("Полезные привычки: ")
    for privuchkiy in privuchki:
        print(privuchkiy)
list_healthy_habits("не пить кофе", "не курить", "не пить алкоголь как свинья даже в праздники")
#####################Задание № 1.6#################
def health_summary(**metric):
    for key, value in metric.items():
        print(f"{key}: {value}")
health_summary(sleep="8 hours", water="1.5 liters", steps=9500)
#####################Задание № 1.7#################
def bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)
print(bmi(70, 1.75))
#####################Блок № 2#################
#####################Задание № 2.1#################
def movie_night_reminder():
    print("Не забудь устроить себе вечер кино!")
movie_night_reminder()
#####################Задание № 2.2#################
def print_movie_rating(movie, raiting):
    print("Фильм", movie, "получил оценку: ", raiting)
print_movie_rating("От заката до рассвета", 10)
#####################Задание № 2.3################
def calculate_watch_time(episodes, duration):
    return episodes * duration
minutes = calculate_watch_time(10, 45)
print(minutes)
#####################Задание № 2.4#################
def plan_movie_session(movie="Inception", snack="попкорн"):
    print(f"Фильм на сегодня: {movie}, а закуска к фильму - {snack}")
plan_movie_session("От заката до рассвета", "чипсы")
plan_movie_session()
#####################Задание № 2.5#################
def list_favorite_movies(*movies):
    print("Любимые фильмы: ")
    for movie in movies:
        print(f"- {movie}")
list_favorite_movies("Обитель зла", "Криминальное чтиво", "От заката дорассвета")
#####################Задание № 2.6#################
def prepare_movie_night(snack="попкорн", *movies):
    print("Ты выбрал закуску: ", snack)
    if len(movies) == 0:
        print("Фильмы пока не выбраны")
    else:
        print("Заплонированные фильмы")
        for movie in movies:
            print(f"- {movie}")
prepare_movie_night("пицца", "От заката до рассвета", "Криминальное чтиво")
print()
prepare_movie_night()
#####################Задание № 2.7#################
def series_info(**detalies):
    for key, value in detalies.items():
        print(f"{key}: {value}")

series_info(tittle="Breaking Bad", seasons=5, genre="Crime, Drama")
#####################Задание № 2.8#################
def average_episode_duration(total_time: int, total_series: int) -> float:
    return total_time / total_series

print(average_episode_duration(150, 10))
#####################Задание № 2.9#################
def movie_night_reminder():
    print("Сегодня у вас киновечер: ")
def plan_movie_session(films="Побег из тюрьмы", food="чипсы"):
    print(f"Фильм сегодня: {films}, а закуски: {food}")

def movie_marathon_plan():
    movie_night_reminder()
    plan_movie_session("От заката до рассвета", "начос")

movie_marathon_plan()