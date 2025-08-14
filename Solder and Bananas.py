k, n, w = map(int, input().split())
total = 0

for i in range(1, w + 1):  # start from 1, not 0
    total += i * k

total_borrow = total - n

# Output the amount to borrow, or 0 if no borrowing is needed
if total_borrow > 0:
    print(total_borrow)
else:
    print(0)