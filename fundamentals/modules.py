# a module is basically a file containing a set of functions to include in your application. here are core python modules, modules you can install using the pip package manager (including Djano), as well as other custom modules.

# core moddules
import datetime
from datetime import date
from time import time

# pip modules
import camelcase

# custom modules
import validator
from validator import validate_email

# date
# today = datetime.date.today()
# today = date.today()
# print("Today's date is:", today)

# # time
# timestamp = time()
# print("The time is:", timestamp)

# # make your text camel case
# camel = camelcase.CamelCase()
# text = "hello there world"
# print(camel.hump(text))

# udsing custom modules
email = "test@test.com"
if (validate_email(email)):
    print("Email passes !")
else:
    print("Email is not valid!!")
