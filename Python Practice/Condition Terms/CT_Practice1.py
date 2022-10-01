print("""
          Calculator
          
          Processes
              
              1- Addition
              2- Subtraction
              3- Multiplication
              4- Division
              
      """)


a= int (input("Please enter the first number "))

b= int (input("Please enter the second number "))

processes= int(input("Enter the processes"))



if (processes==1): 
    
    print(a,"+",b,"=",a+b)

elif (processes==2):
    
    print(a,"-",b,"=",a-b)

elif (processes==3):
    
    print(a,"*",b,"=",a*b)


elif (processes==4):
    
    print(a,"/",b,"=",a/b)
    
else:
    print("False ")