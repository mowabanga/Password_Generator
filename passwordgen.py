import secrets
import string

#generate random letters, digits and characters using string module
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

#concatenate the variables to make characters
password = upper + lower + digits + special_chars

#length of password
pass_length = 8

#use loop to make password
pswd = ''
for i in range(pass_length):
    pswd += ''.join(secrets.choice(password))
    
print(pswd)