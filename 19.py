n = int(input("Введите количество предметов: "))
s = 0
for i in range(0, n):
    x = int(input("оценка за предмет " + str(i + 1) + ":"))
    s += x
average = s / n
print("Средний балл ученика:", average)
#Пользователь вводит количество навчальных предметов n а потом оценки ученика с n предметов вызначыты середнью оценку 