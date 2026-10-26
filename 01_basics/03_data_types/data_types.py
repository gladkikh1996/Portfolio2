#############Задание № 2###################
my_list = [1, 2, 3, 4, 5]
print(my_list, type(my_list))
my_list[0] = 5
print(my_list, type(my_list))
###################Задание № 3 ##########################

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple, type(my_tuple))
try:
    my_tuple[0] = [5]
except TypeError:
    print("Кортеж неизменяем: присвоить новое значение его элементу нельзя.")
print(my_tuple, type(my_tuple))

###################Задание № 4##########################

my_set = {1,2,3,4,5}
print(my_set, type(my_set))

################Задание № 5############################

my_list = [1,2,2,4,5]
new_set = set(my_list)
print(new_set, type(new_set))  #Удалились дублирующие значения, set проводит проверку на уникальность

###################Задание № 6##############

my_dict = {"Июнь": 30, "Июль": 31, "Август": 31}
print(my_dict, type(my_dict))

#################Задание № 7###########################

my_range = range(1, 11)
print(list(my_range), type(my_range))

###########Задание № 8#################################

a = 15
b = "25"

sum_result = a + int(b)
print(sum_result, type(sum_result))

password_letters = "mypassword"
password_digits = 1234
password = password_letters + str(password_digits)
print(password, type(password))
