d1 = {
    'Petrenko':[10, 9, 8, 1, 2],
    'Kmitenko':[12, 9, 9, 10, 5],
    'Ivanov':[1, 2, 3, 6, 7],
    'Yavonsky':[3, 9, 10, 2, 4]
}
av1 = (sum(d1['Petrenko'])/len(d1['Petrenko']))
av2 = (sum(d1['Kmitenko'])/len(d1['Kmitenko']))
av3 = (sum(d1['Ivanov'])/len(d1['Ivanov']))
av4 = (sum(d1['Yavonsky'])/len(d1['Yavonsky']))

av5 = {
    'Petrenko':av1,
    'Kmitenko':av2,
    'Ivanov':av3,
    'Yavonsky':av4
}
print(av5)