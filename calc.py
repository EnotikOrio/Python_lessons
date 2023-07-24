#112
def g(x, h, d):
    if d == "+":
        return x + h
    elif d == "-":
        return x - h
    elif d == "*":
       return x * h
    elif d == "/":
        return x / h
    else:
        print("Такої дії нема")

def j(x, h):
    if x > h:
        return "перше більше"
    elif x < h:
        return "друге число більше"
    else:
        return "вони однакові"
    