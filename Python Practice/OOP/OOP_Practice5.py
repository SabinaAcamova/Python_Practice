class isciler():
    
    def __init__(self,ad,soyad,no,maas):
        
        print("İscilər class-ının init funksiyası..")
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.maas=maas
        
    def information(self):
        print("""
              İsci informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
        
class direktorlar(isciler):
    
    def __init__(self,ad,soyad,no,maas,insan_sayi):
        super().__init__(ad,soyad,no,maas) 
        
        self.insan_sayi= insan_sayi 
        
    def information(self):
        print("""
              Direktor informasiyaları
              
              Ad:{}
              Soyad:{}
              No:{}
              Maas:{}
              """.format(self.ad,self.soyad,self.no,self.maas,))
    
    def maas_artir(self,zam_miqdari):
        
        print("Maas artırıldı")
    
        self.maas += zam_miqdari
isci1=isciler("Walter", "White", 3646474, 10000)
direktor1=direktorlar("Sabina", "Ajamova", 720990, 13131313,13)

isci1.information()
direktor1.information()

