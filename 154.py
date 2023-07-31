f1 = open("nums.txt", "r")
res = open("res.txt", "w")
data = f1.read()
arr1 = []
flag = False
s = ""
for i in data:
    s = s + i
    if i == " " and flag == False:
        flag = True
        arr1.append(int(s[0:len(s) - 1:]))
        s = ""
        flag = False
x = sum(arr1)
res.write(str(x))
print(x)