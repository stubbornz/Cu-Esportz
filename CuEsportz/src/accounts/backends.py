# # importing libraries
# from cryptography.fernet import Fernet

# CRYPTOGRAPHY_KEY = b'2PuVwD1y6cfKo-dsw8sm3BorZpNYPBWY4v1VvKnMJ0I='

# print(CRYPTOGRAPHY_KEY)

# cipher = Fernet(CRYPTOGRAPHY_KEY)
# print(cipher)

# name = "hritik".encode()
# encrypt_file = cipher.encrypt(name)

# print(encrypt_file)




# importing libraries
from django.contrib.auth.models import User

# generating username and returning username, getting name as string
def generateUserName(name):
    # reading total number of users 
    with open('templates/totaluser.txt', 'r') as file:
        total = file.read()
        total_user = int(total)

    # adding all users in list
    users = []
    i = 1
    for i in range(1, total_user + 1):  # only need to fix it
        try:
            obj = User.objects.get(id=i)
        except: pass
        users.append(str(obj))

    # if name exists
    if name in users:
        username = name + str(total_user)
        return username
    else: return name


