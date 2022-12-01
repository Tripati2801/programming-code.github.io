import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobproject.settings')
import django
django.setup()

from jobapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumber():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Teamlead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','phd'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumber()
        hydjob_record=hydjob.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phone_number=fphonenumber)
        bang_record=bangjob.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phone_number=fphonenumber)
        chenjob_record=chenjob.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phone_number=fphonenumber)
populate(100)    
               