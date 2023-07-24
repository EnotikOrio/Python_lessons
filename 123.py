def creat_seasons():
    seasons = {1:"winter",
               2:"spring",
               3:"summer",
               4:"autumn"}
    return seasons


def show_seasons(x):
    s = creat_seasons()
    if x in s:
        return s.get(x)
    else:
        return "no data"
print(show_seasons(int(input("введіть номер сезону: "))))