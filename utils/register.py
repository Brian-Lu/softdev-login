import hashlib

def register(username, password):
    inStream = open("data/login.csv", "a +")
    data = inStream.readlines()
    for item in data:
        currentUser = item.rsplit(",", 1)
        if currentUser[0] == username:
            return "Username already taken bud"
    inStream.write(username + "," + hashlib.sha224(password).hexdigest() + '\n')
    return "Successfully registered"
