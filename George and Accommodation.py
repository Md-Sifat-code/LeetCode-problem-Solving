number_of_testcase = int(input())
count = 0

for _ in range(number_of_testcase):
    x, y = map(int, input().split())
    if y - x >= 2:
        count += 1

print(count)
