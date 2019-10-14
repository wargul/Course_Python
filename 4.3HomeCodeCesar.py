c_code = input("COD ...? y or n ?")
s_text = input("Write message ...")
s_code = int(input("Write Code ..."))

l_text=list("".join(s_text))
for i in range(len(s_text)):
   # print(s_text[i], ord(s_text[i]))
   if c_code == "y":
      if ("A" <= l_text[i] <= "Z") or ("a" <= l_text[i] <= "z"):
         l_text[i] = chr((ord(l_text[i]) + s_code))
   else:
      if ("A" <= l_text[i] <= "Z") or ("a" <= l_text[i] <= "z"):
         l_text[i] = chr((ord(l_text[i]) - s_code))

   print(l_text[i], end="")




