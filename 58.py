x = ["Яблуко", "Банан", "Слива"]
print(x)

g = "Груша"
x.append(g)
print(x)

x.insert(2, 'Айва')
print(x)

fruits = x
print(fruits)

print(fruits.index('Груша'))

fruits.insert(5,"Ананас")
fruits.insert(6,"Манго")
fruits.insert(7,"Черешня")
fruits.insert(8,"Полуниця")
fruits.insert(9,"Абрикос")
print(fruits)

fruits = fruits * 5
print(fruits)

fruits.pop(2)
print(fruits)

b = set(fruits)
print(b)

b.pop()
print(b)

print(fruits.count("Банан"))

while fruits.count("Банан") > 0:
    fruits.remove("Банан")
print(fruits)

f = ["Картопля", "Цибуля", "Морква", "Редис"]

x.extend(f)
print(x)

h = len(fruits)
print(h)

fruits.sort()
print(fruits)

v = len(x[0][0])
print(v)
print(x[0][0])



animals = []

for _ in range(5):
    animal = input("Введіть назву тварини: ")
    animals.append(animal)

animals.sort()

rem = [animals.pop(2), animals.pop()]

dup = rem * 4

com = animals + dup

total = len(com)

tot = sum(len(animal.replace(" ", "")) for animal in com)

print("Список тварин:", com)
print("Кількість всього вийшло тварин:", total)
print("Кількість всього вийшло літер:", tot)
