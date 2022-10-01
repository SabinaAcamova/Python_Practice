class Proqramist():
    
    def __init__(self,ad,soyad,no,maas,diller):
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
        self.diller=diller 

    def information(self):
        print("""
              Proqramist informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              Diller:{}
              """.format(self.ad,self.soyad,self.no,self.maas,self.diller))

proqramist1= Proqramist("Samir","Quliyev",41893127,30000,["Matlab","Fortran","C++","C#","Java","Python"])
proqramist1.information() 
print(" ")

proqramist2= Proqramist("Jon","Stark",422127,2000,["Matlab","C++","C#","Java"])

proqramist2.information() 

