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

class direktorlar(isciler):
    
    def maas_artir(self,zam_miqdari):
        
        print("Maaş artırıldı")
        
        self.maas += zam_miqdari
isci1=isciler("Walter", "White", 3646474, 10000)
direktor1=direktorlar("Sabina", "Ajamova", 720990, 13131313)
isci1.information()
direktor1.information()
direktor1.maas_artir(10000)
direktor1.information()


