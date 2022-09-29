import re
# ------------------------------------------Email Validation -------------------------------------
def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        print("Invalid email / Username ")
        return False
# -----------------------------------------Password Validation ---------------------------------------
def password_check(passwd):      
    SpecialSym =['$', '@', '#', '%']
    val = True      
    if len(passwd) <= 5:
        print('length should be at least 6')
        val = False          
    if len(passwd) >= 16:
        print('length should be not be greater than 16')
        val = False          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
# ---------------------------------------------------Registration -----------------------------------
def registration(email,passwd):
    with open("UserDetails.txt","a") as user:
        user.write(f"{email},{passwd}\n") 
        print("Registration Succsefully")
# --------------------------------------------------Login -------------------------------------------
def login(email,passwd):
    with open("UserDetails.txt","r") as user:
        usernames = []
        passwds = []
        details = {}
        for i in user:
            a,b = i.split(",")
            details[a] = b.removesuffix("\n")
        if email in details.keys():
            if details[email] == passwd:
                print("login Succsefully"  )
            else:
                print("Invalid Details")
                registerOrForrgetPasswd = input("Chosse 1 for Registration 2 for Forget password")
                if registerOrForrgetPasswd == "1":
                    email = input("Enter Email / Username : - ")
                    passwd = input("Enter Password : - ")
                    if isValid(email) and password_check(passwd):                    
                        registration(email,passwd)
                elif registerOrForrgetPasswd == "2":
                    # email = input("Enter Email / Username : - ")
                    if email in details.keys():
                        print(f"Password for {email} is {details[email]}")
                    else:
                        newregisteration = input("Chosse 1 for New Registration")
                        if newregisteration == "1":
                            email = input("Enter Email / Username : - ")
                            passwd = input("Enter Password : - ")
                            if isValid(email) and password_check(passwd):                    
                                registration(email,passwd)
        else:
            print("Username/Email Password is wrong")
# --------------------------Main -----------------------------------------------------------------------------
print("Welcome, please select an option")
loginOrRegistration = input("Choose 1 for Login or 2 for Registration")


if loginOrRegistration == "1":
    email = input("Enter Email / Username : - ")
    passwd = input("Enter Password : - ")
    login(email,passwd)
elif loginOrRegistration == "2":
    email = input("Enter Email / Username : - ")
    passwd = input("Enter Password : - ")
    if isValid(email) and password_check(passwd):
        registration(email,passwd)
else:
    print("Please enter a valid parameter")


