import json
import re

emailregex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Functions ###

# Validaing Email
def checkEmail(email):  
    if(re.search(emailregex, email)):  
        return True      
    else:  
        return False 

# check if user is registered
def isUserRegistered():
    while True:
        userinput = input("Sind Sie bereits angemeldet? ('y' oder 'n'): ")
        if userinput == 'y':
            return True
        elif userinput == 'n':
            return False

# Register new user
def register():
    print("Registrieren Sie sich.")
    while True:
        # Benutzername und Email eingeben lassen
        login_email = input('Ihre Email eingeben: ')
        if checkEmail(login_email) == False:
            print('Ungültige Email')
            continue
        login_username = input('Benutzernamen aussuchen: ')
        # ggf. wiederholen, falls email oder benutzername bereits exisitert
        alreadyExist = False
        for user in users:
            username = users[user][0]['username']
            email = users[user][0]['email']
            if email == str.lower(login_email):
                print(login_email, "ist bereits registriert!") 
                alreadyExist = True
                break        
            elif username == str.lower(login_username):
                print(login_username, "ist bereits vergeben!")
                alreadyExist = True
                break
        if alreadyExist == True:
            continue
        # passwort eingeben lassen und kodieren
        login_password = input('Passwort aussuchen: ')
        # premiummitgliedschaft eingeben lassen
        wantsPremium = None
        while wantsPremium == None:
            userinput = input("Wollen Sie eine Premiummitgliedschaft? ('y' oder 'n'): ")
            if userinput == 'y':
                wantsPremium = True
            elif userinput == 'n':
                wantsPremium = False
        break
    # alle informationen in users.json speichern
    index = len(users) + 1
    userString = 'user' + str(index)
    users[userString] = [{"username" : login_username, "email" : login_email, "password" : login_password,  "isPremiumMember" : wantsPremium}]
    with open('users.json', 'w') as outfile:
        json.dump(users, outfile)
    # einloggen lassen
    login()

# Check valid login
def login():
    print("Loggen Sie sich ein.")
    login_name = input('Benutzernamen oder Email eingeben: ')
    login_password = input('Passwort eingeben: ')
    for user in users:
        username = users[user][0]['username']
        email = users[user][0]['email']
        password = users[user][0]['password']
        isPremium = users[user][0]['isPremiumMember']
        if (username == str.lower(login_name) or email == str.lower(login_name)) and login_password == password :
            if isPremium:
                print("Herzlich Willkommen zur Ihrer Premiummitgliedschaft", username + "!")
                return True
            print("Herzlich Willkommen", username +"!")
            return True
    print("Login Fehlgeschlagen")
    login()

# encode password
def encode():
    pass

#############################################################################################
### MAIN CODE ###############################################################################
#############################################################################################

# User list that initially imports every user from 'users.json' to dic
json_file = open('users.json', 'r', encoding='utf-8')
users = json.load(json_file)
json_file.close()

# Check whether user is registered or not
isRegistered = isUserRegistered()

# register or login the user
if isRegistered:
    login()
else:
    register()



