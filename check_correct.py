import re # import re module - re module provides support for regular expressions 

# Python program to validate an Email 
# Make a regular expression for validating an Email
regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
      
# Define a function for validating an Email
def check_email(email):
    if(re.search(regex_email, email)): # pass the regular expression and the string in search() method 
        return 1
    else:  
        return -1

# Python program to check if given mobile number is valid 

regex_phone = '(05)[0-9]{8}' # Begins with 05, Then contains 10 digits 

def check_number(phone_num): 

    if(re.search(regex_phone, phone_num)): # pass the regular expression and the string in search() method 
        return 1
    else:  
        return -1

regex_digits = '^[0-9\.]*$' # Only digits 

def check_digits(string_digits):
    if(re.search(regex_digits, string_digits)): # pass the regular expression and the string in search() method 
        return 1
    else:  
        return -1

# test
if __name__ == '__main__' :
    email = "shayuo100@gmail.com" # Enter the email
    testt = check_email(email) # calling run function  
    print(testt)

    s = "0548522292" # Enter the number phone
    te=check_number(s)
    print(te)

    s = "0548522292h"
    x = check_digits(s)
    print(x)
 