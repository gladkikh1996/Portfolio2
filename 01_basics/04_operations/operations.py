##############Задание № 2#####################
x = 10

x > 8 and x > 25
x > 8 and x < 25
x < 8 and x < 25
x < 8 and x > 25

x > 8 or x > 25
x > 8 or x < 25
x < 8 or x < 25
x < 8 or x > 25

not(x < 8 and x < 25)
not(x > 8 or x < 25)
print(not(x < 8 and x < 25))
print(not(x > 8 or x < 25))
#############################################
x = 4

x >= 4 and x > 16
x > 4 and x < 16
x <= 4 and x < 16
x < 4 and x > 16

x >= 4 or x > 16
x > 4 or x < 16
x < 4 or x < 16
x <= 4 or x > 16

not(x > 4 and x < 16)
not(x <= 4 or x < 16)
print(not(x > 4 and x < 16))
print(not(x > 4 or x < 16))
###########################################

a = "hello"
b = ""

a and b
a or b

a = [1, 2, 3]
b = [4, 5, 6]

a and b
a or b

print(a and b)
print(a or b)

###########Задание № 3######################

a = True
b = False

print(a and b or not a and not b)
print(not (a or b) and (a or not b))
print(a and not b) or (b and not a)

#####################Задание № 4###############################

x, y = 5, 10
print(y > x * x or y >= 2 * x and x < y)
x, y = 3, 7
print(not (x * 2 == y or y - x < 2))
x, y = 4, 2
print(x > y and y != 0 or x / y > 3)

################Задание № 5########################

x = 9
if x >= 9 and x < 18:
    print(True)
else:
    print(False)

x = 19
if x >= 9 and x < 18:
    print(True)
else:
    print(False)

x = 20
if x <= 23 or x > 60:
    print(True)
else:
    print(False)

###################Задание № 6####################

a = 5
b = -2
result = (a is not None) and (b is not None) and (a > 0 or b > 0)
print(result)
c = 2
result1 = (a % 2 == 0) and (n % 4 != 0)
print(result1)
x = 10
y = None
result2 = (y is not None and x > 0) or not (x < 5)
print(result2)  #y будет None тут False, x больше 0 тут True в итоге False and True = False. В левой части получаем False. В правой части x меньше 5 - False и not = True. С помощью or соединяем False or True = True.

