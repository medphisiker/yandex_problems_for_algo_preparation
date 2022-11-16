# O(n)
str1 = input()
str2 = input()


def calc_sym(string):
    dct = {}

    for sym in string:
        if sym not in dct:
            dct[sym] = 1
        else:
            dct[sym] += 1

    return dct


dct1 = calc_sym(str1)
dct2 = calc_sym(str2)

if dct1 == dct2:
    print(1)
else:
    print(0)
