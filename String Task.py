s = input()
vowels = "aoyeuiAOYEUI"
result = []

for char in s:
    if char not in vowels:
        result.append('.' + char.lower())

print(''.join(result))