import random

numbers = [random.randint(1, 100) for _ in range(10)]
sum_of_numbers = sum(numbers)

print(f"Список чисел: {numbers}")
print(f"Сумма чисел: {sum_of_numbers}")
