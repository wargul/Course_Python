ll = ["spam", "eggs" , 100, 12.5]

for item in ll:
    print(item, type(item))
print()

for n, item in enumerate(ll):
    if n == 2:
        print(n, ll[n:])

for n, item in enumerate(ll):
    if n !=2:
        continue
    print(n, ll[n:])

ll2 = ll + ["Hello"]
print(ll2)

ll3 = ll2*3
print(ll3)