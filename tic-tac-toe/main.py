import random


x_won = False
y_won = False
draw = False
t1 = 0

def show_feald():
    for i in range(0, len(feald)):
        for j in range(0, len(feald[i])):
            print(feald[i][j],end="\t")
        print()


feald = [["*","*","*"],
         ["*","*","*"],
         ["*","*","*"]]
show_feald()

while x_won == False and y_won == False and draw == False:
    x, y = map(int, input("Введіть коорденати: ").split())
    feald[x - 1][y - 1] = "X"
    t1 += 1
    print()
    pc_x = random.randint(1, 3)
    pc_y = random.randint(1, 3)
    while feald[pc_x - 1][pc_y - 1] == "X" or feald[pc_x - 1][pc_y - 1] == "0":
        pc_x = random.randint(1, 3)
        pc_y = random.randint(1, 3)
        print(pc_x)
        print(pc_y)
    feald[pc_x - 1][pc_y - 1] = "0"
    show_feald()
    t1 += 1
    if (feald[0][0] == "X" and feald[0][1] == "X" and feald[0][2] == "X" or 
        feald[1][0] == "X" and feald[1][1] == "X" and feald[1][2] == "X" or
        feald[2][0] == "X" and feald[2][1] == "X" and feald[2][2] == "X" or

        feald[0][0] == "X" and feald[1][0] == "X" and feald[2][0] == "X" or
        feald[0][1] == "X" and feald[1][1] == "X" and feald[2][1] == "X" or
        feald[0][2] == "X" and feald[1][2] == "X" and feald[2][2] == "X" or

        feald[0][0] == "X" and feald[1][1] == "X" and feald[2][2] == "X" or
        feald[0][2] == "X" and feald[1][1] == "X" and feald[2][0] == "X"
        ):
        x_won = True
        print("Х виграв")
    elif (feald[0][0] == "0" and feald[0][1] == "0" and feald[0][2] == "0" or 
        feald[1][0] == "0" and feald[1][1] == "0" and feald[1][2] == "0" or
        feald[2][0] == "0" and feald[2][1] == "0" and feald[2][2] == "0" or

        feald[0][0] == "0" and feald[1][0] == "0" and feald[2][0] == "0" or
        feald[0][1] == "0" and feald[1][1] == "0" and feald[2][1] == "0" or
        feald[0][2] == "0" and feald[1][2] == "0" and feald[2][2] == "0" or

        feald[0][0] == "0" and feald[1][1] == "0" and feald[2][2] == "0" or
        feald[0][2] == "0" and feald[1][1] == "0" and feald[2][0] == "0"
        ):
        y_won = True
        print("0 виграв")
    elif t1 == 9:
        draw = True
        print("Нечья")
