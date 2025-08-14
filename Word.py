s = input()
uppercase = sum(1 for ch in s if ch.isupper())
lowercase = len(s) - uppercase
 
if uppercase > lowercase:
    print(s.upper())
else:
    print(s.lower())