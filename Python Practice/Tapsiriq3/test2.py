import module2
import math
print("""
          Calculator
          
          Processes
              
              1. Toplama
              2. Çıxma
              3. Bölme
              4. Vurma
              5. EBOB Tapma
              6. EKOB Tapma
              7. 2 Ededin Toplamının Faktorialını Tapma (Fakt(a+b) )
              
              'q' Proqramdan cixis
      """)

while True: 
    processes= input("Enter the processes")
    if (processes=="q"):
        print("Proqramdan cixilir...")
        break
    elif (processes=="1"):
        a=int(input("\na: "))
        b=int(input("\nb2: "))
        one=module2.toplama(a,b)
        print(one)
    
    elif (processes=="2"):
        a=int(input("\na: "))
        b=int(input("\nb: "))
        two=module2.cixma(a,b)
        print(two)
    elif (processes=="3"):
        a=int(input("\na: "))
        b=int(input("\nb: "))
        three=module2.bolme(a,b)
        print(three)

    elif (processes=="4"):
        a=int(input("\na: "))
        b=int(input("\nb: "))
        four=module2.vurma(a,b)
        print(four)
    
    elif (processes=="5"):
        a=int(input("\na: "))
        b=int(input("\nb: "))
        five=module2.ebob(a,b)
        print(five)
    elif (processes=="6"):
        a=int(input("\na: "))
        b=int(input("\nb: "))
        six=module2.ekob(a,b)
        print(six)
    elif (processes=="7"):  
        a=int(input("\na: "))
        b=int(input("\nb: "))
        n =a+b
        one=module2.toplama(a,b)
        seven=module2.factorial(n)
        print(seven)
    else:
        print("False ")
