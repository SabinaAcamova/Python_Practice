print(" LOGIN\n")

name= "WalterWhite"

password= "13122002"


user_name= input("Enter your user name:  ")

user_password = input ("Enter your password:  ")


if ( user_name!=name and  password== user_password): 
    
    print("Your username is incorrect. ")

elif (user_name ==name and password != user_password): 

    print("Your password is incorrect. ")

elif (user_name !=name and password != user_password): 

    print("Your username and password are incorrect. ")

else:
    print("True")
