from collections import Counter

y = int(input())

def has_all_distinct_digits(year):
    digit_counts = Counter(str(year))
    return all(count == 1 for count in digit_counts.values())
    
y +=1

while not has_all_distinct_digits(y):
    y += 1

print(y)