t = 0
for r in range(0, 17):
    for o in range(0, 31):
        for l in range(0, 41):
            if r * 15 + o * 8 + l * 4 == 240:
                print("Ручек:",r ,"Олывців:",o ,"Ластиків:", l)
                t = t + 1
print("Кількість комбінацій:", t)









#Ручка коштує 15 грн; олівець 8 грн; ластик 4 грн вивести всі можливі варіації які можно придбати на 240 грн