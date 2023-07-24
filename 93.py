Capitals = {

}
Capitals['Ukraine'] = 'Kyiv'
Capitals['USA'] = 'Washington'
Capitals['Germany'] = 'Berlin'
Capitals['Japan'] = 'Tokyo'
Capitals['Switzerland'] = 'Berne'
Countries = ['Ukraine', 'USA', 'Poland', 'Germany', 'France', 'Japan', 'Switzerland']
for x in Countries:
    if x in Capitals:
        print("The capital of", x, Capitals[x])
    else:
        print("This country", x, "is not on the list")