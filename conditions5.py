email = input("enter your email")
if '@' in email and len(email) >= 11 and ('.com' in email or 'org' in email):
    print("valid email")
else:
    print("invalid email")