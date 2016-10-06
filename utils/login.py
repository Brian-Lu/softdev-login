import hashlib

def login(username, password):
    data = open("data/login.csv", "r")
    for line in data:
        indexOfPassword = line.find(',')
        if line[:indexOfPassword] == username and line[indexOfPassword + 1:] == hashlib.sha224(password).hexdigest() + '\n':
            return "You have successfully logged in, " + username
        elif line[:indexOfPassword] == username:
            return "Wrong password??? Try again!!!"
    return "Wrong username??? Try again!!!"

