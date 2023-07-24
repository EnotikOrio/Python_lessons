s = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0

for p1 in range(2, 8):
    for p2 in range(2, 8):
        for p3 in range(2, 8):
            for p4 in range(2, 8):
                for p5 in range(2, 8):
                    for p6 in range(2, 8):
                        if p1 + p2 + p3 - p4 + p5 + p6 == 15:
                            print(p1, p2, p3, p4, p5, p6)
                            s += 1

print("Колво паролей:", s)
