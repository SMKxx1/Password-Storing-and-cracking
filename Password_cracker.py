import hashlib

def encoder(password):
    password1 = hashlib.md5(password.encode())
    password = password1.hexdigest()
    return password

def login():
    count = 0
    while count < 3:
        user = input("Enter your username: ")
        password = input("Enter your password: ")
        password = encoder(password)
        user_pass_dictionary = str({user: password})
        if user_pass_dictionary in open("Password.txt").read():
            print()
            print("You are logged in now!!!")
            def secret_create():
                secret = input("Enter your secret: ")
                f = open("Password.txt", "r")
                lines = f.readlines()
                f.close()
                f = open("Password.txt", "w")
                for line in lines:
                    if line != str({user: password}) + "\n":
                        f.write(line)
                f.write(str({user: password}) + " " + secret + "\n")
                print("Your secret has been saved!!!")
                f.close()
            def secret_change():
                secret = input("Enter your new secret: ")
                f = open("Password.txt", "r")
                lines = f.readlines()
                f.close()
                f = open("Password.txt", "w")
                for line in lines:
                    if line != str({user: password}) + "\n":
                        f.write(line)
                f.write(str({user: password}) + " " + secret + "\n")
                print("Your new secret has been saved!!!")
                f.close()
            secret_create()
            secret_change()
            break
        else:
            print("Invalid Username or Password!!!")
            count += 1
            if count != 3:
                print("You have", 3 - count, "more attempts left")
                print()
            elif count == 3:
                print("Too many attempts...")
                break

def pass_creator():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    password = encoder(password)
    f = open("Password.txt","a+")
    user_pass_dictionary = str({user:password}) + "\n"
    f.write(user_pass_dictionary)
    print("Your username and password has successfully been added")

def pass_changer():
    user = input("Enter your username: ")
    pass_old = input("Enter your old password: ")
    pass_old = encoder(pass_old)
    if str({user:pass_old}) in open("Password.txt").read():
        pass_new = input("Enter your new password: ")
        pass_new = encoder(pass_new)
        f = open("Password.txt","r")
        lines = f.readlines()
        f.close()
        f = open("Password.txt","w")
        for line in lines:
            if line != str({user:pass_old})+"\n":
                f.write(line)
        f.write(str({user: pass_new}))
        f.close()
        print("Your password has been successfully changed")
    else:
        print("Invalid username or password")



def pass_reader():
    user_name = input("Enter the username: ")
    password = input("Enter the password: ")
    password1 = hashlib.md5(password.encode())
    password = password1.hexdigest()
    dictionary = str({user_name:password})
    if dictionary in open("Password.txt").read():
        print("Credentials Found!!!")
    else:
        print("Credentials Not Found!!!")

attempted_password = ""

def brute():
    cc = 0
    list_of_chars = "\[\{\]\}'\:0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "
    def solve_password(word):
        global attempted_password
        for character in word:
            for entry in list_of_chars:
                if character == entry:
                    attempted_password += character
                    print(attempted_password)
                    continue
        return attempted_password

    print("Enter the username to Bruteforce")
    user = input("> ")
    user = "{'"+user+"':"
    f = open("Password.txt","r")
    lines = f.readlines()
    f.close()
    f = open("Password.txt","r")
    for line in lines:
        if user in line:
            password2 = line
            password = solve_password(password2)
            if password in open("Password.txt").read():
                print()
                print("You have successfully Bruteforced into the account")
            else:
                print("Bruteforce failed...")
            cc += 1
        else:
            pass
    if cc == 0:
        print(cc)
        print("No user found...")
    else:
        pass



def main():
    print("Please choose your option bellow")
    print("Enter 1 to create an username and password")
    print("Enter 2 to login using your username and password")
    print("Enter 3 to change your password")
    choice = input("> ")
    if choice == '1':
        pass_creator()
    elif choice == '2':
        login()
    elif choice == '3':
        pass_changer()
    elif choice == 'Brute' or 'brute':
        brute()
    else:
        pass


login()
