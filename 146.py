#Перевести число у вісімкову систему численя рекурсією
def dec(num):
    if num == 0:
        return '0'
    elif num < 8:
        return str(num)
    else:
        return dec(num // 8) + str(num % 8)

dec1 = int(input("Введіть десяткове число: "))
oct = dec(dec1)
print(f"Вісімкове число: {oct}")
