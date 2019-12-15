import os
from django.core.wsgi import get_wsgi_application

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
print(sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mainApp.settings')
application = get_wsgi_application()

from CAAT.models import Profile, Complaints
from django.contrib.auth.models import User

for username in ['student', 'electrician', 'carpenter']:
    print("Deleting {}".format(username))
    try:
        user = User.objects.get(username=username)
        user.delete()
    except:
        pass
    print("Deleted {}".format(username))
