import re
s = input("Enter Identifier to validate : ")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9]*',s)
if m != None:
   print(s,"is valid yava identfier")
else:
   print(s,'is not valid yava identifier')   