#############Задание № 1#########
salt = "морская"

def cook_pasta():
    salt = "поваренная"
    print("Внутри функции: ", salt)

cook_pasta()
print("Теперь снаружи: ", salt)
#############Задание № 2#########
pepper = "черный"

def change_pepper():
    pepper = "красный"
    print("Внутри: ", pepper)

change_pepper()
print("Снаружи: ", pepper)   #Глобальную переменную не меняли, а создали новую локальную переменную pepper
#############Задание № 3#########
pepper = "черный"

def change_pepper():
    global pepper
    pepper = "красный"
    print("Внутри: ", pepper)

change_pepper()
print("Снаружи: ", pepper)  #Тут мы уже поменяли глобальную переменную
#############Задание № 4#########
oil = "оливковое"

def cook_salad():
    oil = "подсолнечное"
    print("Внутри функция: ", oil)

cook_salad()
print("Снаружи функция: ", oil)
#############Задание № 5#########
# eggs = 10
#
# def use_eggs():
#     eggs = eggs - 1  #При запуске будет UnboundLocalError, так как переменная eggs внутри функции становится локальной и python не может присвоить ей значение.
#     print("Внутри функции: ", eggs)
#
# use_eggs()
# print("Снаружи функции: ", eggs)
#############Задание № 6#########
eggs = 10

def use_eggs():
    global eggs  # с добавлением global функция стала изменять глобальную переменную eggs.
    eggs = eggs - 1
    print("Внутри функции:", eggs)

use_eggs()
print("Снаружи функции:", eggs)
#############Задание № 7#########
def make_marinade():
    sauce = "кисло-сладкий"

    def add_secret_ingredient():
        sauce = "соевый"
        print("Изменение на ", sauce)

    add_secret_ingredient()
    print("Внутри функции make_marinade: ", sauce)

make_marinade()    #Во вложенной функции создаласть новая локальная переменная sauce поэтому внутри add_secret_ingridient() выводится соевый но переменная sauce в make_marinade не меняется и остается прежней - "кисло-сладкий"
#############Задание № 8#########
def make_marinade():
    sauce = "кисло-сладкий"

    def add_secret_ingredient():
        nonlocal sauce
        sauce = "соевый"
        print("Изменение на ", sauce)

    add_secret_ingredient()
    print("Внутри функции make_marinade: ", sauce)

make_marinade()   #После добавления nonlocal вложенная функция add_secret_ingredient меняет переменную sauce из внешней функции make_marinade
#############Задание № 9#########
def main_recipe():
    spice = "карри"

    def step():
        def detail_step():
            nonlocal spice
            spice = "паприка"
            print("Внутри функции detail_step: ", spice)

        detail_step()
    step()
main_recipe()
#############Задание № 10#########
# def recipe():
#     def inner():
#         nonlocal new_ing
#         new_ing = "шоколад"
#
#     inner()
#
# recipe()  #Будет ошибка SyntaxError: no binding for nonlocal 'new_ing' found потому что nonlocal можно использовать только для переменной которая есть во внешней функции, а тут переменной new_ing снаружи нету.
#############Задание № 11#########
def prepare():
    main_ing = "томат"
    spice = "базилик"

    def adjust():
        nonlocal spice
        spice = "орегано"
        print("Внутри функции adjust: ", main_ing, spice)

    adjust()
    print("После изменений в функции adjust: ", main_ing, spice)

prepare()  #из-за nonlocal переменная spice изменится с базилика на орегано.
#############Задание № 12#########
def pantry():
    stock = {"sugar": 5}

    def update_stock():
        nonlocal stock
        stock["sugar"] += 1

    update_stock()
    print(stock)

pantry()
#############Задание № 13#########
flour = "пшеничная"

def bake_cake():
    flour = "кукурузная"

    def step():
        print("Внутри step():", flour)

    step()
    print("Внутри bake_cake():", flour)

print("Снаружи функции:", flour)
bake_cake()
print("Снаружи функции после вызова:", flour)
#############Задание № 14#########
def make_dough():
    yeast = "сухие"

    def activate_yeast():
        yeast = "живые"
        print("Внутри функции activate_yeast: ", yeast)

    activate_yeast()
    print("После изменений в функции make_dough: ", yeast)

make_dough()
#############Задание № 15#########
# sugar = 100
#
# def bake():
#     sugar = sugar + 10
#     print(sugar)
#
# bake()  #UnboundLocalError: cannot access local variable 'sugar' where it is not associated with a value, так как sugar внутри функции является локальной переменной.
# #############Задание № 16#########
spice = "паприка"

def outer():
    spice = "карри"
    def inner():
        print("Вывожу spice внутри inner: ", spice)

    inner()
    print("После измнений вывожу spice внутри inner: ", spice)

outer()
print("Снаружи функции: ", spice)








