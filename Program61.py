# print ASCII table

def ASCIITable():
    print("*"*10,"ASCII Value Table","*"*10)
    print("Decimal\tASCII Value")
    
    for i in range(1,127+1):
        print(i,"\t",chr(i))
    print("*"*30)    
        
ASCIITable()        