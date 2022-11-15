import datetime
import os
import pickle
import shutil

from buttons_targets import show_the_statistics, target_image_process
from camera_fun import clean_target_picture

default_bullets_num = (12,)

class Person:
    def __init__(self, name_person, id_num, email_address, phone_num):
        self.name_person = name_person
        self.id_num = id_num
        self.email_address = email_address
        self.phone_num = phone_num
        self.num_targets = 0
    
    def get_name(self):
        return self.name_person

    def get_id(self):
        return self.id_num

    def get_email_address(self):
        return self.email_address

    def get_phone_num(self):
        new_phone = '"+972' + self.phone_num[1:] + '"'
        return new_phone

    def set_num_targets_plus_one(self):
        if self.num_targets < 3 :
            self.num_targets += 1

    def get_num_targets(self):
        return self.num_targets


class DataBase:
    def __init__(self):
        self.users_dict = {} #### to users_dict
        fname = 'filename.pickle'
        if (os.path.isfile(fname)):
            with open('filename.pickle', 'rb') as handle:
                self.users_dict = pickle.load(handle)

    def get_user(self, email_address):
        if email_address in self.users_dict:
            return self.users_dict[email_address]
        else:
            return -1

    def add_user(self, name_person, id_num, email_address, phone_num):
        fname = 'filename.pickle'
        if (os.path.isfile(fname)):
            with open('filename.pickle', 'rb') as handle:
                dictionary = pickle.load(handle)
                self.users_dict = dictionary
                print(self.users_dict)

        if email_address.strip() not in self.users_dict:
            person = Person(name_person.strip(), id_num.strip(), email_address.strip(), phone_num.strip())
            self.users_dict[email_address.strip()] = person

            with open('filename.pickle', 'wb') as handle:
                pickle.dump(self.users_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

            self.make_dir(email_address, id_num)
            return 1
        else:
            print("email exists already")
            return -1

    def get_users_dict(self):
        return self.users_dict

    def validate(self, email_address, id_num):
        if self.get_user(email_address) != -1:
            return self.users_dict[email_address].get_id() == id_num
        else:
            return False

    def make_dir(self, email_address, id_num):
        parent_dir = os.getcwd()+"/Users/"
        path = os.path.join(parent_dir, id_num)
        if(not(os.path.isdir(path))):
            os.mkdir(path)

    def remove_dir(self, email_address, id_num):
        del self.users_dict[email_address]
        parent_dir = os.getcwd()+"/Users/"
        path = os.path.join(parent_dir, id_num)
        if(os.path.isdir(path)):
            shutil.rmtree(path)

    def activate_target_image_process(self, email_address, target_num, bullets_number):
        #pass
        if bullets_number == "":
            bullets_number = default_bullets_num[0]
        self.users_dict[email_address].set_num_targets_plus_one()
        phone_num = self.users_dict[email_address].get_phone_num()
        name_user = self.users_dict[email_address].get_name()
        num_id = self.users_dict[email_address].get_id()
        target_image_process(phone_num, name_user, email_address, num_id, target_num, bullets_number)

    def new_target_picture(self):
        clean_target_picture()

    def send_statistics(self, email_address):
        #pass
        num_id = self.users_dict[email_address].get_id()
        num_targets = self.users_dict[email_address].get_num_targets()
        print(num_targets)
        check_success = show_the_statistics(email_address, num_id, num_targets)
        return check_success

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


# test
"""if __name__ == '__main__' :
    with open('filename.pickle', 'rb') as handle:
        dicto = pickle.load(handle)
    
    #print(dicto)


    #first
    namep1="shaynitzan"
    idnum1="209403344"
    email1="shayuo@gmail.com"
    phone1= "0523393453"
    #second
    namep2="dudu"
    idnum2="205699257"
    email2="duud@gmail.com"
    phone2= "0543699625"

    #shaynitzan = Person(namep1, idnum1, email1, phone1)
    #print(shaynitzan.get_email_address())
    #dudu = Person(namep2, idnum2, email2, phone2)
    #print(dudu.get_email_address())

    users_db = DataBase()
    print(users_db.get_users_dict())

    users_db.add_user(namep1, idnum1, email1, phone1)
    users_db.add_user(namep2, idnum2, email2, phone2)
    users_db.add_user(namep2, idnum2, email2, phone2)

    print(users_db.get_user(email1).get_name())
    print(users_db.get_users_dict())

    print(users_db.validate(email1, idnum1))
    print(users_db.validate(email1, 209403347))
    print ("Current working dir : %s" % os.getcwd())"""