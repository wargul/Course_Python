s = "Hello its me \"call\" you"
print(s)
print(len(s))
print(s[0])

for i in range(len(s)):
    print(s[i], end="")
print()

print(s[0:4])
print(s)


s = s.lower()
print(s.lower())
print(s.replace("world", "taras"))
print(s)

print(s[1::4])
print(s)

s[::-1]
print(s)

s = "hello 1111 2222 3333 4444"
s_spl = s.split(0)
print(s_spl)
s_spl[1]
print(s_spl)


