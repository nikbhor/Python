#Display Byte

def DisplayByte(iNo):
    Byte1 = iNo & 0x000000FF
    
    Byte2 = iNo & 0x0000FF00
    Byte2 = Byte2 >> 8
    
    Byte3 = iNo & 0x00FF0000
    Byte3 = Byte3 >> 16
    
    Byte4 = iNo & 0xFF000000
    Byte4 = Byte4 >> 24
    
    print(Byte1)
    print(Byte2)
    print(Byte3)
    print(Byte4)

if __name__=="__main__":
   iValue = int(input("Enter Number : "))
   DisplayByte(iValue)   