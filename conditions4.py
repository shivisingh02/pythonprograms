email = input("enter your emeail :")
if '@' in email:
    if len(email) >= 11:
        if ".com" in email or "org" in email:
            print("your email is valid")
        else:
            print("invalid email")
    else:
        print("length of your email not valid")
else :
    print("your email does not have @")

