bord = [1]
print(bord)

#let_bord = bord+[3, 5, -10]

bord.extend([3, 5, 6, 7, 8, 9, -10])
print(bord)

print(len(bord))
print(bord.index(3))

let_in = bord.index(5)
print(bord[let_in-1], bord[let_in+1])
print("next")

n = 0
for i in range(len(bord)):
    if (n == 2):
        print()
        n = 0
    n = n + 1

    print(bord[i], end=" ")

print("next")

for h in range(len(bord)):
    if (h%2) == 0:
        print()
    print(bord[h], end="\t")

let_hop = bord.index(5)
let_hip = bord.index(-10)

print("next")

x = bord[let_hop]
bord[let_hop] = bord[let_hip]
bord[let_hip] = x
print(bord)

print("next")

bord[let_hop], bord[let_hip] = bord[let_hip], bord[let_hop]
print(bord)
print("next")

ll = []
for i in range(10):
    ll.append(i)
print(ll)

