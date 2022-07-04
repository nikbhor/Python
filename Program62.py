# print ASCII table decimal hexadecimal octal and character

def ASCIITable():
    print("*"*10,"ASCII Value Table","*"*10)
    print("Decimal\tHexadecimal\tOctal\tASCII Value")
    
    for i in range(1,127+1):
        print(i,"\t",hex(i),"\t",oct(i),"\t",chr(i))
    print("*"*60)    
        
ASCIITable()        