#Взяти довільну розповідь, зберегти їі в текстовому файлі знайти яка літера зустрічается най частіше в тексті а також яка зустрічаєтся менше за всіх 

f1 = open('story.txt', 'r')
t = f1.read()
f1.close()

l = {}
for l1 in t:
    if l1.isupper() or l1.islower():
        l[l1] = l.get(l1, 0) + 1

m = max(l, key=l.get)
l2 = min(l, key=l.get)

print(f"Найчастіше зустрічається літера: {m}")
print(f"Зустрічається менше за всіх літера: {l2}")

