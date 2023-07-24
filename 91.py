dicrionary = {
    'food':'spaghetti',
    'drink':'juice',
    'cutlery':'fork'
}
dicrionary_2 = {
    'spices':'paper',
    'sauce':'mayonnaise'
}
print(dicrionary['drink'])
print()
print(dicrionary)
print()
dicrionary['drink'] = 'milk', 'water'
print(dicrionary)
print()
dicrionary['drink'] = 'milk'
print(dicrionary)
print()
dicrionary.update(dicrionary_2)
print(dicrionary)
print()
print(dicrionary['food'])
print(dicrionary.get('food'))
'''print(dicrionary['dsdsd'])
print(dicrionary.get('scd'))'''
dicrionary.pop('food')
print(dicrionary)
print(dicrionary.keys())
print(dicrionary.values())
print(dicrionary.items())
print(dicrionary.clear())
print(dicrionary.copy())
print(dicrionary.fromkeys())
print(dicrionary.get())
print(dicrionary.items())