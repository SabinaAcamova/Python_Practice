password = 1312
balance = 13000
while True:
    try:
        input_password=int(input("Please enter your password: "))
    except ValueError:
        print("Zehmet olmasa reqemlerden ibaret kod daxil edin!")
        continue
    if(password==input_password):
        print("""
              
                 ATM
              Processes:
                  1.Balansi goster
                  2.Hesaba depozit
                  3.Pul cekmek
              
              'q' Proqramdan cixis
              
              """)
    break
while True:
    process = input("Enter process: ")
    
    if (process=="q"):
        print("Proqramdan cixilir...")
        break
    elif (process=="1"):
        print("Balansiniz {} manat".format(balance))
    elif (process=="2"):
        miqdar=int(input("Elave etmek istediyiniz mebleg: "))
        balance+=miqdar
        print("Balansiniz {} manat".format(balance))
    elif (process=="3"):
        miqdar=int(input("Cekmek istediyiniz mebleg: "))
        if(balance-miqdar<0):
           print("Kartda bu qeder pul yoxdur!!!")
           continue
        balance-=miqdar
        print("Balansiniz {} manat".format(balance))
    else:
        print("Dogru prosesi daxil edin")
        
