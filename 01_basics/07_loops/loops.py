###########Задание №1.1#################
x = "Python is the best programming language"
for word in x.split():
    if len(word) <= 3:
        continue
    print(word)
#########Задание №1.2##################
for x in range(15, 101):
    if x % 13 == 0:
        break
    print(x)
########Задание №1.3####################
for x in range(1, 31):
    if x % 5 == 0:
        print(x)
#####Задание №1.4###############
for x in range(1, 101):
    for y in range(1, 101):
        if x + y == 50:
            print(x, y)
            break
#######Задание №1.5############
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})", end=" ")
    print()
#####Задание №2.1#############
x = "вереВкА, спИчки, коМПАс, нАвигатор, фОнАрик, гореЛкА, рюкзАк, спальнИк, палаткА"
items = x.split(", ")
for item in items:
    print(item)
######Задание№ 2.2#############
x = backpack = "вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
items = x.split(", ")
for item in items:
    print(item.capitalize())
#######Задание №2.3##############
x = "вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
items = x.split(", ")
i = 0
while i < len(items):
    word = items[i]
    print(word[::-1])
    i += 1
##########Задание №2.4################
backpack = "Одеяло, вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
for item in backpack.split(", "):
    if item[0] in vowels:
        print(item)
############Задание №2.5##############
backpack = "Одеяло, вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
item = backpack.split(", ")
i = 0
while i < len(item):
    print(item[i].lower())
    i += 1
##########Задание №2.6############
backpack = "Одеяло, вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
items = backpack.split(", ")
long = ""
for item in items:
    if len(item) > len(long):
        long = item
print(long)
#########Задание №2.7##########
backpack = "Одеяло, вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
items = backpack.split(", ")
i = 0
while i < len(items):
    if len(items[i]) > 7:
        items.pop(i)
    else:
        i += 1
print(items)
#############Задание № 2.8#############
backpack = "Одеяло, вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
items = backpack.split(", ")
i = 0
while i < len(items):
    items[i] = items[i] + "!"
    i += 1
print(items)
