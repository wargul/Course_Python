ll = [2, 25]
print (ll)

ll.append(45)
print(ll)

ll.extend([32, 67, 89])
print(ll)
ll.append([32, 67, 89, 66, 77, 88])
print(ll.append(5))
print(ll)

position = ll.index(32)
print(32, " plased in ", position, "-th position", sep="")
print(f"{32} plased in {position}-th position")

#ll.remove(25)
ll.remove(2)
print(ll)

item = ll.pop(0)
#print(item)
print(ll)
print(f"The length of the list is {len(ll)} items.")

ll = [2, 67, 33, 45]
ll.sort()
print(ll)

ll.reverse()
print(ll)