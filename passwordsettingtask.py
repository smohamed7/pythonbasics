#An application that asks a user a string password
#if the characters are less than five print too short
#if the characters are greater than five show too long


password = str(input("type in your password:"))
if len(password)<5:
    print("yours password is too short")
elif len(password)>15:
    print("password too long")
elif len(password) >=5 and len(password) <=15:
    print("success")
else:
    print("INVALID")


#


