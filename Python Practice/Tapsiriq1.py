pin = 1312
balance = 13000
print("Welcome")
choice = 9

while (True):
    print("0.Cixis")
    print("1.Balansi goster")
    print("2.Pul Yatirma")
    print("3.Pul Cixarma")

    choice = int(input("Proses nomresini daxil edin "))

    if choice == 0:
       print("You have been logged out. Thank you!") 
       break
   # try:
       input_pin = int(input("Zehmet olmasa Pininizi daxil edin: "))\
   # except ValueError:
      #  print("Zəhmət olmasa inputları doğru daxil ediniz.")
    if input_pin == pin:
        if choice == 1:
           print("Balansiniz: ",balance)
           continue
        if choice == 2:
           miqdar = int(input("Yatırmak istediginiz miqdar: "))
           balance += miqdar
           print("Bakiyeniz {} tldir".format(balance))
           continue
        if choice == 3:
           cix_miqdar = int(input("Cekmek istediginiz miqdar: "))
           if (balance - cix_miqdar < 0 ):
                print("Bu qeder pul ceke bilmezsiniz")
                print("Bakiyeniz {} tldir".format(balance))
                continue
           balance -= cix_miqdar
           print("Bakiyeniz {} tldir".format(balance))
        else:
            print("Yanlis Proses")
            continue
    else:
        print("Yanlis PIN")
     
















