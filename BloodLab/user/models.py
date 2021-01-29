from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User as AuthUser 
# Create your models here.

class User (models.Model) :
    user = models.OneToOneField( AuthUser, on_delete=models.CASCADE, primary_key=True)
    sex = models.BooleanField()
    phone = models.CharField(max_length=11, validators=[RegexValidator(regex=r"^\w{11}$", message="phone number length must be 11")])

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name) 

class Lab (models.Model) :
    name = models.CharField(primary_key=True, max_length=50) 
    end_point = models.URLField()
    api_key = models.TextField()

    def __str__(self):
        return str(self.name)
    

class BloodExpert (User) :
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    
    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name) 

class TimeService (models.Model) :
    expert_snn = models.ForeignKey(BloodExpert, on_delete=models.CASCADE)
    date = models.DateField()
    stime = models.TimeField()
    etime = models.TimeField()
    evailable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.date) + "\t ===>\t" + \
            str(self.stime) + " till " + \
            str(self.etime) 
    

    class Meta : 
        unique_together = (("expert_snn", "date", "stime", "etime"))

    def clean (self) :
        super().clean()
        if self.stime > self.etime :
            raise ValidationError(message="start time is further than end time!")

    


