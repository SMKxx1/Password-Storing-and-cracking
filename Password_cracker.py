import hashlib
import fileinput
import sys
import os
import time
import Art
import getpass

clear = lambda: os.system('cls')

def replace(file, searchexp, replaceexp):
    for line in fileinput.input(file, inplace=1):
        if searchexp in line:
            line = line.replace(searchexp, replaceexp)
        sys.stdout.write(line)

def encoder(password):
    password1 = hashlib.md5(password.encode())
    password = password1.hexdigest()
    return password

def secret_create(user, password):
    secret = input("Enter your secret: ")
    for line in open("Password.txt").readlines():
        if user in line and password in line:
            sec = line
            sec = sec.split(' ')
            try:
                sec[2] = secret + "\n"
                sec = sec[:3]
            except:
                sec.append(secret + "\n")
            try:
                a = sec[1]
                a = a.rstrip('\n')
                sec[1] = a
            except:
                pass
            sec = ' '.join(sec)
            replace("Password.txt",line,sec)
        else:
            pass
    Art.ext("Your secret has been saved","!")
    clear()

def secret_read(user, password):
    count = 0
    for line in open("Password.txt").readlines():
        if user in line and password in line:
            sec = line.split()[2:]
            sec = ' '.join(sec)
            print("Your secret is:", sec)
            count += 1
            input()
            clear()
        else:
            pass
    if count == 0:
        print("Error:", "No secret created")
        clear()
    else:
        pass

def login2(user, password):
    print('''What do you want to do??
1. Create a secret
2. Read a secret
3. Change your Password
4. Logout''')
    ch = input('> ')
    if ch == '1':
        secret_create(user, password)
        login2(user, password)
    elif ch == '2':
        secret_read(user, password)
        login2(user, password)
    elif ch == '4':
        Art.ext("Logging out",".")
        main()
    elif ch == '3':
        pass_changer(user,password)
    else:
        print("I didn't quite get that")
        login2(user, password)

def login():
    count = 0
    while count < 3:
        user = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ", stream=None)
        password = encoder(password)
        user_pass_dictionary = str({user: password})
        clear()
        if user_pass_dictionary in open("Password.txt").read():
            print()
            Art.login_art()
            print("Welcome {0}!!!".format(user))
            print()
            login2(user,password)
        else:
            Art.ext("Invalid Username or Password","!")
            count += 1
            if count != 3:
                print("You have", 3 - count, "more attempts left")
                print()
            elif count == 3:
                Art.ext("Too many attempts",".")
                break

def pass_creator():
    user = input("Enter your username: ")
    if "{'" + str(user) + "':" in open("Password.txt").read():
        Art.ext("Username already taken","!")
        clear()
        main()
    else:
        password = getpass.getpass("Enter your password: ",stream=None)
        re_password = getpass.getpass("Re-enter your password",stream=None)
        if password == re_password:
            password = encoder(password)
            f = open("Password.txt", "a+")
            user_pass_dictionary = str({user: password})
            f.writelines("\n" + user_pass_dictionary)
            Art.ext("Your username and password has successfully been added",".")
            f.close()
            clear()
            main()
        else:
            Art.ext("Passwords don't match",".")
            main()

def pass_changer(user,password):
    pass_old = getpass.getpass("Enter your old password: ",stream=None)
    pass_old = encoder(pass_old)
    if str({user: pass_old}) in open("Password.txt").read():
        pass_new = getpass.getpass("Enter your new password: ",stream=None)
        pass_new_re = getpass.getpass("Re-enter your new password: ",stream=None)
        if pass_new == pass_new_re:
            pass_new = encoder(pass_new)
            replace("Password.txt", str({user: pass_old}), str({user: pass_new}))
            print("Your password has been successfully changed")
        else:
            Art.ext("Passwords does not match",".")
            login2(user,pass_new)
    else:
        Art.ext("Invalid username or password",".")
        login2(user,password)

def pass_reader():
    user_name = input("Enter the username: ")
    password = input("Enter the password: ")
    password1 = hashlib.md5(password.encode())
    password = password1.hexdigest()
    dictionary = str({user_name: password})
    if dictionary in open("Password.txt").read():
        print("Credentials Found!!!")
    else:
        print("Credentials Not Found!!!")

attempted_password = ""

def brute_login(user, password):
    print()
    clear()
    Art.login_art()
    print("Welcome {0}!!!".format(user))
    print()
    def login2(user, password):
        print('''What do you want to do??
1. Create a secret
2. Read a secret
3. Change your Password
4. Logout''')
        ch = input('> ')
        if ch == '1':
            secret_create(user, password)
            login2(user, password)
        elif ch == '2':
            secret_read(user, password)
            login2(user, password)
        elif ch == '4':
            Art.ext("Logging out",".")
            main()
        elif ch == '3':
            pass_changer(user,password)
        else:
            print("I didn't quite get that")
            login2(user, password)

    login2(user, password)

def brute():
    Art.brute_art()
    cc = 0
    list_of_chars = "\[\{\]\}'\:0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "

    def solve_password(word):
        global attempted_password
        print()
        while True:
            for i in word:
                for char in list_of_chars:
                    attempted_password += char
                    print(attempted_password,end='\r')
                    time.sleep(0.01)
                    if char == i:
                        pass
                    else:
                        attempted_password = attempted_password[:-1]
            if attempted_password == word:
                break
            else:
                pass
        return attempted_password

    print("Enter the username to Bruteforce")
    user = input("> ")
    user = "{'" + user + "':"
    for line in open("Password.txt").readlines():
        if user in line:
            password2 = line.split("'")[3]
            password = solve_password(password2)
            if password in open("Password.txt").read():
                print()
                print("You have successfully Bruteforced into the account")
                user = user[2:-2]
                print(user)
                brute_login(user, password)
            else:
                print("Bruteforce failed...")
            cc += 1
        else:
            pass
    if cc == 0:
        print(cc)
        print("No user found...")
        input()
        main()
    else:
        pass

def main():
    clear()
    Art.name()
    print("Please choose your option bellow")
    print("Enter 1 to create an username and password")
    print("Enter 2 to login using your username and password")
    print("Type 'ext' to exit")
    choice = input("> ")
    if choice == '1':
        clear()
        pass_creator()
    elif choice == '2':
        clear()
        login()
    elif choice == 'ext':
        Art.ext("Have a Good Day","!")
        clear()
        exit()
    elif choice == 'brute':
        clear()
        brute()
    else:
        Art.ext("I did'nt quite get that",".")
        clear()
        main()

main()
