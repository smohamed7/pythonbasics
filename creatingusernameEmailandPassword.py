#createUsername
#create Email
#create password
#login to facebook

username ="mark"
email = "mark@gmail.com"
password =123456

print("---LOGIN TO FACEBOOK---")

user = input("enter username: ")

if user == username:
   em = input("enter email: ")
   if em == email:
       passw =int(input("password: "))
       if passw == password:
           print("suceesful login")
       else:
           print("wrong password")

   else:
       print("wrong email")

else:
    print("wrong username")
