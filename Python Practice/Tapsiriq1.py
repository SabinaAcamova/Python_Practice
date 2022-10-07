
print("Welcome to the Bank")
p=int(input("Enter your pin number: "))
money = 13000
if(p == 1312):
  print("1-Balans Sorğulama")
  print("2-Pul Yatırmaq")
  print("3-Pul Çekmek")
  c = int(input("Proses secin: "))
else:
    print("Wrong password")
     
  if (processes== "q"): 
  print("Hesabdan cixis")
  break
  elif(c==1):
  print("Bakiyeniz : ",m)
  elif (c == 2):
    miqdar = int(input("Yatırmak istediginiz miqdar: "))

    bakiye += miqdar
    print("Bakiyeniz {} tldir".format(bakiye))
  elif (c == 3):
    miktar = int(input("Cekmek istediginiz miqdar: "))
    if (bakiye - miqdar < 0 ):
        print("Bu qeder pul ceke bilmezsiniz")
        print("Bakiyeniz {} tldir".format(bakiye))
        continue
    bakiye -= miktar
    print("Bakiyeniz {} tldir".format(bakiye))
else:
   print("Zehmet olmasa dogru prosesi girin!.")

