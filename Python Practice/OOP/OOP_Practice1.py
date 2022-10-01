class Avtomobil (): 
    
    def __init__(self,model,reng,at_gucu,silindir_sayi): 
        
        self.model= model 
        self.reng = reng 
        self.at_gucu= at_gucu
        self.silindir_sayi = silindir_sayi 
        
avtomobil1=  Avtomobil("Tesla","Qara",300,6)

print("Avtomobilin modeli: ", avtomobil1.model)
print("Avtomobilin rengi: ", avtomobil1.reng)
print("Avtomobilin at gucu: ", avtomobil1.at_gucu)
print("Avtomobilin silindir sayi: ", avtomobil1.silindir_sayi)
        
print(" ")

avtomobil2= Avtomobil("BMW","Yasil", 250,4)

print("Avtomobilin modeli: ", avtomobil2.model)
print("Avtomobilin rengi: ", avtomobil2.reng)
print("Avtomobilin at gucu: ", avtomobil2.at_gucu)
print("Avtomobilin silindir sayi: ", avtomobil2.silindir_sayi)


print(type(avtomobil1))
print(type(avtomobil2))