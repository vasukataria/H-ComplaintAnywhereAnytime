import os
from django.core.wsgi import get_wsgi_application

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
print(sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainApp.settings')
application = get_wsgi_application()

from CAAT.models import Profile, Complaints
from django.contrib.auth.models import User

print("Creating student")
student = User.objects.create_user('student', password='1234', email='student@gmail.com',
                                   first_name='Vasu', last_name='Kataria')
Profile.objects.create(user=student, type='STUDENT')
print("Created student with id={}, username={}".format(student.id, student.username))


print("Creating electrician")
electrician = User.objects.create_user('electrician', password='1234', email='electrician@gmail.com',
                                   first_name='Electrician FName', last_name='Electrician LName')
Profile.objects.create(user=electrician, type='ELECTRICIAN')
print("Created electrician with id={}, username={}".format(electrician.id, electrician.username))


print("Creating carpenter")
carpenter = User.objects.create_user('carpenter', password='1234', email='carpenter@gmail.com',
                                       first_name='carpenter FName', last_name='carpenter LName')
Profile.objects.create(user=carpenter, type='CARPENTER')
print("Created carpenter with id={}, username={}".format(carpenter.id, carpenter.username))

