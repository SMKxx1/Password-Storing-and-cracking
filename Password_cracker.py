import hashlib
def pass_creator():
    password = input("Enter a password: ")
    password1 = hashlib.md5(password.encode())
    f = open("Password.txt","a+")
    password2 = password1.hexdigest()
    password2 = "\n" + password2
    f.write(password2)
    f.close
pass_creator()