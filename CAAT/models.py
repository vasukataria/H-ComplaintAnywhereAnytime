from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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
        ('CARPENTER', 'Carpenter'),
        ('PLUMBER', 'plumber'),
        ('AIR_CONDITIONER','Air_conditioner'),
        ('ROOM_CLEANING','Room_cleaning')
        
    )
    HOSTEL_TYPES = [
        ('L', 'L')
    ]
    
    FLOOR_TYPES = [
        ('1','1'),
        ('2','2'),
        ('3','3')
    ]

    GENDER_TYPES = [
        ('MALE','Male'),
        ('FEMALE','Female'),
        ('OTHER','Other')
    ]
    

    # Django OneToOne field: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    type = models.CharField(max_length=50, choices=USER_TYPES)

    dob = models.DateField(null=True)

    Hostel = models.CharField(max_length=10 ,choices=HOSTEL_TYPES ,null=True)
    Floor = models.CharField(max_length=10 ,choices=FLOOR_TYPES ,null=True)
    Room_number= models.IntegerField(null=True)
    Gender=models.CharField(max_length=11, choices=GENDER_TYPES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+919999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)


    def can_workon(self):
        # Eg. complaint of type ELECTRICITY is handled by ELECTRICIAN
        return {
            'ELECTRICIAN': 'ELECTRICITY',
            'CARPENTER': 'CARPENTER',
            'PLUMBER' : 'PLUMBER',
            'AIR_CONDITIONER':'AIR_CONDITIONER',
            'ROOM_CLEANING' : 'ROOM_CLEANING'

        }.get(self.type)

class Feedback(models.Model):
    RATING_TYPES =[
        ('EXCELLENT','Excellent'),
        ('VERY-GOOD','Very-good'),
        ('GOOD','GOOD'),
        ('AVERAGE','Average'),
        ('POOR','Poor')
    ]

    details = models.TextField()
    date = models.DateField(auto_now_add=True)
    Rating=models.CharField(max_length=11, choices=RATING_TYPES)
 

