n, h = map(int, input().split())
heights = list(map(int, input().split()))

total_space_need = 0
for height in heights:
    if height <= h:
        total_space_need += 1
    else:
        total_space_need += 2

print(total_space_need)
