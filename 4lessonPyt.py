s = """Hello its me . \t "call" you
Not you but im. """

ss = s.split(" ")
print(ss)

j_ss = "#".join(ss)
print(j_ss)

print("capitalize:", s.capitalize())
print("upper", s.upper())
print("title", s.title())
print("lower", s.lower())

if s.startswith("A"):
    print("Starts from \"A\"")
else:
    print("I dont know from where")
