def ebob_tapma(eded1,eded2):
    i = 1
    ebob = 1
    while (i <= eded1 and i <= eded2 ): 

        if ( not (eded1 % i) and not (eded2 % i)):
            print(ebob)
            ebob = i
        i += 1
    return ebob
eded1 = int(input("Eded 1:"))
eded2 = int(input("Eded 2:"))
print("Ebob:",ebob_tapma(eded1,eded2))