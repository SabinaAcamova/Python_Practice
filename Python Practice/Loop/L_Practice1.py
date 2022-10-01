print("""
      Faktorial Hesablama
      
      Cıxmaq ucun "q" a basın.
          
      """)
while True :
    
    reqem = input("Reqemi daxil edin: ")
    
    if(reqem=="q"):
        
        print("Proqramdan cıxılır")
        
        break
    reqem= int(reqem)
    fakt=1
  
    for i in range(2,reqem+1):
        fakt *= i 

    print("Faktorial:",fakt)
    
    