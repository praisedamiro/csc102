username = input("what is your name: ")
password = input("Enter your password: ")
confirm_password = input("please confirm your password: ")
is_running = True

while is_running:
    if password == confirm_password:
        print('Password validated')
        is_running = False
    else:
        print('Passowrd is invalid')
        confirm_password = input("please confirm your password: ")
        if password == confirm_password:
            print('Password validated')
            is_running = False
