import hashlib

def register(username, password):
    data = open("data/login.csv", "a +")
    for line in data:
        indexOfPassword = line.find(',')
        if line[:indexOfPassword] == username:
            return "Username already taken bud"
    data.write(username + "," + hashlib.sha224(password).hexdigest() + '\n')
    data.close()
    return "Successfully registered"
