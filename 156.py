#Записати в файл таблицю яка матиме значення від одного до 25 (подвійний цикл)
f1 = open('table.txt', 'w')
for i in range(1, 26):
    f1.write(f"{i}\t")
    if i % 5 == 0:
        f1.write('\n')
f1.close()
