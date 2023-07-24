#621

def long_word(w1, w2):
    if len(w1) > len(w2):
        return w1
    elif len(w1) == len(w2):
        return w1, w2
    return w2

i = input().split()

w1 = i[0]
w2 = i[1]
print(long_word(w1, w2))