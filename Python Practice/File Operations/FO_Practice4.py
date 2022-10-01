with open("Test1.txt", "r") as fayl:
    print("Kursorumuz bu baytdadr",fayl.tell())
    fayl.seek(15)
    print("Kursorumuz bu baytdadr",fayl.tell())
    oxu_fayl=fayl.read()
    print("Faylin icindeki deger: ",oxu_fayl)
