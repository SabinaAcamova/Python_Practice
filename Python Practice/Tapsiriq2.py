class isciler():
    
    def __init__(self,ad,soyad,no,maas):
        
        print("İşçilər classının init funksiyası...")
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
        
        
    def information(self):
        print("""
         
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
  
class Proqramist(isciler):
    def __init__(self,ad,soyad,no,maas,dil,is_tecrubesi):
        super().__init__(ad,soyad,no,maas) 
        
        self.dil= dil
        self.is_tecrubesi=is_tecrubesi
    def information(self):
        print("""
              Programist informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              Dil:{}
              Is Tecrubesi:{} il
              """.format(self.ad,self.soyad,self.no,self.maas,self.dil,self.is_tecrubesi))
    def dil_elave_et(self,dil):
      
      self.dil.append(dil)

      print("Dil elave olundu...")
class direktorlar(isciler):
    def __init__(self,ad,soyad,no,maas,isci_sayi):
        super().__init__(ad,soyad,no,maas) 
        
        self.isci_sayi= isci_sayi 
        
    def information(self):
        print("""
              Direktor informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              Isci Sayi: {}
              """.format(self.ad,self.soyad,self.no,self.maas,self.isci_sayi))
    
    def maas_artir(self,zam_miq):
        
        print("Maaş artırıldı")
        
        self.maas += zam_miq   
class investorlar(isciler):
    def __init__(self,ad,soyad,no,maas,invst):
        super().__init__(ad,soyad,no,maas) 
        
        self.invst= invst
        
    def information(self):
        print("""
              Investor informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              Invest. meblegi: {}
              """.format(self.ad,self.soyad,self.no,self.maas,self.invst))        
    def invst_miqdari(self,invst_m):
         self.invst += invst_m
isci1=isciler("Walter", "White", 3646474, 10000)
isci1.information()  
direktor1=direktorlar("Sabina", "Ajamova", 720990, 13131313,13)
direktor1.information()
direktor1.maas_artir(10000)
direktor1.information()
proqramist1= Proqramist("Samir","Quliyev",41893127,30000,["Matlab","Fortran","C++","C#","Java","Python"],7)
proqramist1.dil_elave_et("HTML")
proqramist1.information() 
inv1=investorlar("Walter", "White", 3646474, 10000,1000)
inv1.information() 
inv1.invst_miqdari(1000)
inv1.information()
