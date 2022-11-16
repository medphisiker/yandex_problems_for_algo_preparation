n = int(input())

if n > 0:
    # считываем первое число
    curr_num = int(input())
    print(curr_num)

    for i in range(n - 1):
        next_num = int(input())
        if curr_num != next_num:
            print(next_num)
            curr_num = next_num
