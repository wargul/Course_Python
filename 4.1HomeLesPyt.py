s_mon = float(input("How much change is owned ?..."))

s_mon = round(s_mon*100, 0)

print(s_mon)
k = 0
while s_mon > 0:
    if s_mon >= 25:
        s_mon = s_mon - 25
        k = k + 1
    elif s_mon >= 10:
        s_mon = s_mon - 10
        k = k + 1
    elif s_mon >= 5:
        s_mon = s_mon - 5
        k = k + 1
    elif s_mon >= 1:
        s_mon = s_mon - 1
        k = k + 1
    else:
        s_mon = 0

print(k)