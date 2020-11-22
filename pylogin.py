#Saving email id and pass word for login
import pickle
import os
import hashlib

database_file = './db/reginfo.txt'

#in case of opening for the first time or absent database file
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
    _password = pycryp(input('Enter your password: \t'))

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
def pycryp(password):
    salt = os.urandom(32)  # A new salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return (salt, key)


add_user()
print('Successfully Registered')

print('Showing Subscribers')
show_users()
