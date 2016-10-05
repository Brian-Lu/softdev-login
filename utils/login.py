import hashlib

def login(username, password):
    inStream = open("data/login.csv", "r")
    data = inStream.readlines()
    for item in data:
        currentUser = item.strip().rsplit(",", 1)
        if currentUser[0] == username and currentUser[1] == hashlib.sha224(password).hexdigest():
            return "You have successfully logged in, " + username
        else:
            return "Wrong password??? Try again!!!"
    return "Wrong username??? Try again!!!"