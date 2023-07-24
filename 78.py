x = "Hello World, My name is Ivan"
b = "IliveinDnipro"
c = "1234567183847543654536474"
h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
j = "G F A C E I F G Q H J K F F F F F L L L L L L P P P P"
t = 0
print(x[2])
print(x[0::2])
print(x[::-1])
print(x + b)
print(x * 3)
print(len(x))
print(x.find(" ", 6, 13))
print(x.rfind(" "))
print(x.split(" "))
print(c.isdigit())
print(b.isalpha())
print(b.islower())
print(b.isupper())
print(b.istitle())
#print("_".join(h))
print(x.upper())
print(x.lower())
print(x.center(100, "|"))
print(ord("W"))
print(x.count("Hello"))
print(x.lstrip(" "))
print(x.rstrip(" "))
print(x.strip(" "))
print(x.swapcase())
print(x.title())
print(x.count(" ") + 1)
y = j.split()
y.sort()
print(y)

for i in range(0, len(y)):
    if y[i] != j[i]:
        t += 1
if t != 0:
    print("Не відсортовано")
else:
    print("Відсортовано")
    