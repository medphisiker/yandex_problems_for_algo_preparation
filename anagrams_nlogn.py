# O(n*logn)
str1 = input()
str2 = input()

if sorted(str1) == sorted(str2):
    print(1)
else:
    print(0)
