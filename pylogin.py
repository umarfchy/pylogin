#Saving email id and pass word for login
# class RegInfo():
#     def __init__():
#         #make a empty dictionary at first if the obj is not empty
#         pass
# reginfo = reginfo
# if reginfo.pickle in

# try:
#     monday=pickle.load(open("roombooking.bin","rb"))
# except EOFError:
#     monday = []

import pickle
import os

database_file = './db/reginfo.txt'

#in case of opening first time or absent database file
if not os.path.isfile(database_file):
    db_dict = {}
    pickle_out = open(database_file, 'wb')
    pickle.dump(db_dict, pickle_out)
    pickle_out.close()


def add_user():

    #opening the db dictionary obj
    db_dict = pickle.load(open(database_file, 'rb'))

    #reigistration information
    ##email id is the uniq id. So it needs input validation
    _email = input('Enter your email id: \t')
    if _email in db_dict.keys():
        print('This email is already registered.\nTry with a new one.')
        return

    _username = input('Enter your username: \t')
    _password = input('Enter your password: \t')
    db_dict[_email] = (_username, _password)

    #Saving the object for later reference
    pickle_out = open(database_file, 'wb')
    pickle.dump(db_dict, pickle_out)
    pickle_out.close()


def show_users():
    pickle_in = open(database_file, 'rb')
    db_dict = pickle.load(pickle_in)
    print(db_dict)


# Encryption mechanism
# function => Encryption; arg => password

add_user()
print('Successfully Registered')

print('Showing Subscriber')
show_users()
