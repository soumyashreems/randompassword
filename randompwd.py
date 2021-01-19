import string

from random import *

characters = string.ascii_letters + string.punctuation  + string.digits

password = ""

for x in range(randint(8,12)):
    password += choice(characters)

print(password)