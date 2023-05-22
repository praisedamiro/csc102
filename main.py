username = input("what is your name: ")
password = input("Enter your password: ")
confirm_password = input("please confirm your password: ")

if password == confirm_password:
    print('Password validated')
else:
    while password != confirm_password:
        print('Passowrd is invalid')
        confirm_password = input("please confirm your password: ")
