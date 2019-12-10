from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
COMPLAINTS_TYPES = (
    ('ELECTRICITY', 'Electricity'),
    ('PLUMBER','Plumber'),
    ('CARPANTER','Carpanter'),
    ('AIR_CONDITIONER', 'Air_conditioner'),
    ('ROOM_CLEANING', 'Room_cleaning')
)

class Complaints(models.Model):
    type = models.CharField(max_length=100 ,choices=COMPLAINTS_TYPES)
    #room_no = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
       #return "complain {}".format(self.id)
        return "Complaint No. {} ({})".format(self.id, self.type)




    #def __str__(self):
        #return "Complaint of " + self.name

USER_TYPES = (
    ('STUDENT', 'Student'),
    ('ELECTRICIAN', 'Electrician'),
    
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=USER_TYPES)
    dob = models.DateField()
