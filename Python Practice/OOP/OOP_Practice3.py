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

    def dil_elave_et(self,yeni_dil):
        
        self.diller.append(yeni_dil)

        print("Dil elave olundu...")
        
        
    def maas_artir(self,artim_miqdari):
        
        print("Maas artirildi...")
        
        self.maas+=artim_miqdari    
        
proqramist1= Proqramist("Samir","Quliyev",41893127,30000,["Matlab","Fortran","C++","C#","Java","Python"])      

proqramist1.dil_elave_et("HTML")
proqramist1.maas_artir(300)
proqramist1.information() 






