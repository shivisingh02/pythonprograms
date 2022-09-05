email = input("enter your emeail :")
if '@' not in email:
    print("your email does not have @")
elif len(email) < 11:
    print("length is not enough")
elif ".com" not in email and "org" not in email:
    print('invalid domain')
else:
    print("valid email")
            
        