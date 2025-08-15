number = int(input())
count = 0

while number != 0:
    if number % 10 == 4 or number % 10 == 7:
        count += 1
    number //= 10

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
