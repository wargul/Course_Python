#hr = float(input("How time is it ?  "))

#m = hr*60
#s = m*60
#print("Time: "+str(hr)+" "+" All minutes: "+str(m)+" All seconds: "+str(s))

s_name = input("Enter your name :").split(" ")

for i in range(len(s_name)):
    if s_name[i] != "":
        print(s_name[i][0:1].upper(), end=".")

if 3 in range(len(s_name)):
    print(s_name[3])

