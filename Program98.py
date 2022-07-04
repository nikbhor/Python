# Create file

file = input("Enter File name you want to created  : ")

try:
   f = open(file,'x')
   
except FileExistsError:
       print("File Alredy Exists")
else:
    print("File created Successfully")      
finally:
       f.close() 
       print("File Close Successfully")       
