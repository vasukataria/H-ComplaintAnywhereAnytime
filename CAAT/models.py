from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Django Choices: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices

class Complaints(models.Model):
    COMPLAINTS_TYPES = (
        ('ELECTRICITY', 'Electricity'),
        ('PLUMBER','Plumber'),
        ('CARPENTER','Carpenter'),
        ('AIR_CONDITIONER', 'Air_conditioner'),
        ('ROOM_CLEANING', 'Room_cleaning')
    )

    COMPLAINTS_STATUSES = (
        ('NOT_ATTENDED', 'Not Attended'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )

    type = models.CharField(max_length=100, choices=COMPLAINTS_TYPES)

    status = models.CharField(max_length=100, choices=COMPLAINTS_STATUSES, default='NOT_ATTENDED')

    desc = models.TextField()

    # Filepath to images uploaded to the server
    image = models.ImageField(upload_to='pics', null=True)

    # Foreign key relationship with the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # When the complaint was created
    created_at = models.DateTimeField(default=datetime.now)

    # When was the complaint resolved
    resolved_at = models.DateTimeField(null=True)
   
    def __str__(self):
       #return "complain {}".format(self.id)
        return "Complaint No. {} ({})".format(self.id, self.type)


class Profile(models.Model):
    USER_TYPES = (
        ('STUDENT', 'Student'),
        ('ELECTRICIAN', 'Electrician'),
        ('CARPENTER', 'Carpenter')
    )

    # Django OneToOne field: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    type = models.CharField(max_length=50, choices=USER_TYPES)

    dob = models.DateField()

    def can_workon(self):
        # Eg. complaint of type ELECTRICITY is handled by ELECTRICIAN
        return {
            'ELECTRICIAN': 'ELECTRICITY',
            'CARPENTER': 'CARPENTER'
        }.get(self.type)
