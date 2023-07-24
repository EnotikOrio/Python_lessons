#414, 415, 416, 417, 

#414 Знайдіть кількість додатних елементів у введеному списку:


#415 Виведіть всі елементи списку з непарними індексами:
'''arr2 = list(map(int, input().split()))
print(arr2[0::2])'''

'''416 Виведіть ті його елементи, які зустрічаються в списку лише один раз
arr3 = list(map(int, input().split()))
result2 = []
for num2 in arr3:
    if arr3.count(num2) == 1:
        result2.append(num2)
print(result2)'''


#Обчисліть, скільки у списку різних елементів, не змінюючи самого списку
arr4 = list(map(int, input().split()))
print(len(set(arr4)))

'''arr1 = list(map(int, input().split()))
num1 = 0
for i in range(0, len(arr1)):
    if arr1[i] > 0:
        num1 += 1
print(arr1)
print(num1)'''