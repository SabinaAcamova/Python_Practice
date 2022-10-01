bakiye =13000 
while True:
    islem = input("İslemi girin:")

    if (islem == "q"):
        print("Yine bekleriz.")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Yatırmak istediginiz tutar: "))

        bakiye += miktar
        print("Bakiyeniz {} tldir".format(bakiye))
    elif (islem == "3"):
        miktar = int(input("Cekmek istediginiz tutar: "))
        if (bakiye - miktar < 0 ):
            print("Bu kadar para cekemezsiniz.")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= miktar
        print("Bakiyeniz {} tldir".format(bakiye))
    else:
        print("Lutfen gecerli bir islem girin.")
