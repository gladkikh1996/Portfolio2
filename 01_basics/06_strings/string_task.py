###########Задание 1.1##################
radius = 5
height = 10
pi = 3.14159

volume = pi * radius ** 2 * height

print(f"radius = {radius}, height = {height}, pi = {pi} -> V = {volume:.2f}")

#####################Задание 1.2####################

temp_C = 36.6
temp_F = (temp_C * 9 / 5) + 32
print(f"{temp_C:.1f}C = {temp_F:.2f}F")

###############Задание 1.3###################

distance = 185
time = 3

speed = distance / time

print(f"distance = {distance}, time = {time} -> speed = {speed:.2f}")

#########Задание 2.1#################

s1 = "111" * 5
print("s1 =", s1)

s2 = 111 * 5
print("s2 =", s2)

s3 = 111.11 * 5
print("s3 =", s3)

try:
    s4 = "111" * "111"
    print("s4 =", s4)
except TypeError:
    print('s4 = "111" * "111" -> ошибка, строку нельзя умножать на строку')
##########Задание № 2.2################

new_str = "BOdHnKEWDpTFVgqdCkMVZTaQzXQBDjdiufEX"
if new_str.isdigit():
    print(f"{new_str} содержит только цифры")
else:
    if new_str.isalpha():
        print(f"{new_str} содержит только буквы")
    else:
        print(f"{new_str} содержит буквы и цифры и другие символы")

###########Задание № 2.3#############

sentence = "Learning Python is fun and useful"
words = sentence.split()
print(f"{len(words)}")

#########Задание № 2.4##############

sentence = "Learning Python is fun and useful"
words = sentence.split()
joined = "-".join(words)
print(f"{joined}")

##########Блок № 3############

backpack1 = "         	пАлатка, спаЛьник, рЮКзак           	"
backpack2 = "горЕЛка!фОнарик!карта!компАС"
backpack3 = "икЧИпс"
#########3.1###########
backpack1 = backpack1.strip()
print(backpack1)
#########3.2############
backpack2 = backpack2.replace("!", ", ")
print(backpack2)
#######3.3############
id_before = id(backpack3)
print(id_before)
backpack3 = backpack3[::-1]
print(backpack3)
id_after = id(backpack3)
print(id_after)
###############3.4############
backpack1 = backpack1.lower()
print(backpack1)
############3.5#############
items2 = backpack2.split(", ")
first_two = items2[:2]
backpack3 = backpack3 + ", " + ", ".join(first_two)
print(backpack3)
##########3.6##############
items = ((backpack3 + " ") * 3).strip()
print(items)
############3.7################
id_before = id(backpack1)
print(id_before)
print(backpack1)
backpack1 = backpack1 + ", " + backpack2 + ", " + backpack3
id_after = id(backpack1)
print(id_after)
print(backpack1)
##############3.8#################
backpack1 = backpack1.title()
print(backpack1)
##############3.9#################
idx = backpack1.lower().find("карта")
print(idx)
#############3.10###########
count = len(backpack1)
print(f"{count}")
###########3.11#############
items = backpack1.split(", ")
print(items)

