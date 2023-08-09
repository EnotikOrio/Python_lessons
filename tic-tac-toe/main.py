def show_feald():
    for i in range(0, len(feald)):
        for j in range(0, len(feald[i])):
            print(feald[i][j],end="\t")
        print()


feald = [["*","*","*"],
         ["*","*","*"],
         ["*","*","*"]]
show_feald()

while True:
    x, y = map(int, input("Введіть коорденати: ").split())
    feald[x - 1][y - 1] = "X"
    print()
    show_feald()
