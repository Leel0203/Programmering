text = input()
shift = int(input())
result = ""

for c in text:
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        result += chr((ord(c) - base + shift) % 26 + base)
    else:
        result += c

print(result)