#659

def valid_date(day, month, year):
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 12 and 1 <= day <= days_month[month - 1] and year > 0:
        return True
    else:
        return False

d1 = int(input())
m1 = int(input())
y1 = int(input())

res1 = valid_date(d1, m1, y1)
print(res1)
