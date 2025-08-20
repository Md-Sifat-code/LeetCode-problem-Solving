n = int(input())
s = input()

a_count = s.count('A')
d_count = s.count('D')

if a_count > d_count:
    print("Anton")
elif d_count > a_count:
    print("Danik")
else:
    print("Friendship")
