n = int(input())
bin_num = []
for i in range(n):
    bin_num.append(int(input()))

ones_cnt = 0
max_cnt = 0
for num in bin_num:
    if num == 1:
        ones_cnt += 1

    else:
        if max_cnt < ones_cnt:
            max_cnt = ones_cnt

        ones_cnt = 0

else:
    if max_cnt < ones_cnt:
        max_cnt = ones_cnt

print(max_cnt)
