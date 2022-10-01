def tam_bolunenler (eded):
    bolunenler = list()
    
    for i in range (2,eded):
        
        if (eded % i == 0 ):
            
            bolunenler.append(i)
            
    return bolunenler

while True: 
    
    eded = input("Bir eded daxil edin: ")
    
    if (eded == "q"):
        break
    else: 
        eded= int(eded)
        a = tam_bolunenler(eded)
        
        print("Daxil etdiyiniz edede tam bölünen ededler: ",a)