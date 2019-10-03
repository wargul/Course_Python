#height = int(input("Enter height .."))
#for i in range(height):
 #   for k in range(i + 1):
  #      print("#", end="")
   # print()

#height = int(input("Enter height .."))
#for i in range(height):
 #   for k in range(height - i):
#        print("#", end="")
 #   print()

height = int(input("Enter height .."))
for i in range(height):
    for z in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print()