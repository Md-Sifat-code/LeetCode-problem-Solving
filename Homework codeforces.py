t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # length of a
    a = input().strip()
    m = int(input())  # length of b and c
    b = input().strip()
    c = input().strip()

    for i in range(m):
        if c[i] == 'V':
            a = b[i] + a   # Vlad -> add to the beginning
        else:
            a = a + b[i]   # Dima -> add to the end

    print(a)
