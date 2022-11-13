# import os
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

# import os 

# BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR=os.path.join(BASE_DIR, 'templates')
# print(TEMPLATE_DIR)


# import os

# BASE_DIR=os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR=os.path.join(BASE_DIR, 'templates')
# print(TEMPLATE_DIR)

from faker import Faker
from random import*

import faker
fake=Faker()
for i in range (10):
    print(fake.company())
# name = fakegen.name()
# print(name)