##################Задание 1.1######################

x = int(input("Введите число: "))

if x < 0:
    print("Отрицательное")
else:
    print("Положительное или ноль")

x = int(input("Введите число: "))
if x % 2 == 0:
    print("Четное")
else:
    print("нечетное")

x = int(input("Введите число: "))
if x > 100:
    print("Число слишком большое")
else:
    print("Число подходит")

###################Задание 1.2#####################

x = int(input("Напишите время записи в парикмахерскую: "))
if 9 <= x < 18:
    print("Вы записаны!")
else:
    print("Ошибка!")

############Задание № 2.1##############################

x = int(input("Введите число в диапазоне -100 до 100: "))
if x <= -100 or x >= 100:
    print("Ошибка")
elif x < 0:
    print("Отрицательное")
elif x > 0:
    print("Положительное")
else:
    print("Ноль")

#############Задание 2.2####################

x = input("Введите ваш возраст: ")
if not x.isdigit():
    print("Ошибка")
else:
    x = int(x)
    if x <= 0:
        print("Ошибка")
    elif x < 18:
        print("Несовершеннолетний")
    elif 18 <= x <= 59:
        print("Взрослый")
    else:
        print("Пенсионер")

##############Задание №2.3#####################

x = input("Введите число: ")
if not x.isdigit():
    print("Ошибка")
else:
    if x == "5":
        print("Отлично")
    elif x == "4":
        print("Хорошо")
    elif x == "3":
        print("Удовлетворительно")
    elif x == "2":
        print("Плохо")
    elif x == "1":
        print("Очень плохо")
    else:
        print("Таких оценок нет")

##############Задание № 2.4#####################

x = input("Введите ваш возраст: ")
if not x.isdigit():
    print("Введите числовое значение")
else:
    x = int(x)

    if x <= 0:
        print("Ошибка")
    elif x < 23:
        print("Ваша студенческая скидка 20%")
    elif x > 60:
        print("Ваша пенсионная скидка 30%")
    else:
        print("Скидка не предусмотрена")

##########################Задание № 2.5#####################

milk_list_available = ["burenka","prostokvashino", "vkusnoteevo", "happy cow"]
milk_list_not_available = ["domik v derevne", "nasha korova"]
milk = input("Введите название молока: ").lower()
if milk in milk_list_available:
    print("Заказ принят!")
elif milk in milk_list_not_available:
    print("К сожалению, данный продукт закончился")
else:
    print("Мы не продаем данную продукцию")

################Задание № 3.1#######################
x = input("Пользователь № 1 Введите число: ")
y = input("Пользователь № 2 Введите число: ")
if not x.isdigit() or not y.isdigit():
    print("Введите корректные числовые значения")
else:
    x = int(x)
    y = int(y)

    if x > y:
        if y == 0:
            print("Ошибка: деление на ноль невозможно")
        elif x % y == 0:
            print("Делится")
        else:
            print("Не делится")
    elif x < y:
        print("Первое число меньше второго")
    else:
        print("Числа равны")

###########Задание № 3.2#######################

x = input("Введите пароль: ")
if not isinstance(x, str):
    print("Ошибка: пароль должен быть строкой")
elif len(x) < 8:
    print("Слишком короткий пароль")
else:
    if "!" in x:
        print("Надежный пароль")
    else:
        print("Добавьте символы")

##########Задание № 3.3####################

year = input("Введите год: ")
if not year.isdigit():
    print("Ошибка, введите числовое значение")
else:
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")









