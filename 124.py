#623

def find_min_max(n):
    min_n = n[0]
    max_n = n[0]
    for num in n:
        if num < min_n:
            min_n = num
        if num > max_n:
            max_n = num
    return (min_n, max_n)

i = map(int, input("").split())
numbers = []
for num in i:
    numbers.append(int(num))

result = find_min_max(numbers)
print(result)
