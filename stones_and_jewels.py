jewels = input()
stones = input()

jewels_symbols = set(jewels)

counter = 0
for stone in stones:
    if stone in jewels_symbols:
        counter += 1

print(counter)
