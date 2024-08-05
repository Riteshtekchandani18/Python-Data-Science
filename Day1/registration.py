print("Resgistration Application")
username = input ('enter your name')
email = input('enter your email')
password = input ('enter your password')
cpassword = input ('confirm youor password')

if username and email and password and cpassword:
    if username.isalnum():
        if '@'in email and email.endswith('.com'):
            if password==cpassword:
                if len(password)>=8:
                    print("Resgistration compeleted")
                    print("hurrah")
                else:
                    print("password too small")
            else:
                print('password doesnot match')
        else:
            print('invalid email')
    else:
        print('invalid username')
else:
    print('All fields requried')