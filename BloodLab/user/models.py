from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User (models.Model) :
    snn = models.CharField(primary_key = True, max_length = 10 ,validators=[RegexValidator(regex=r"^\w{10}$", message="snn length must be 10")])
    password = models.CharField(max_length=10) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.BooleanField()
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex=r"^\w{11}$", message="phone number length must be 11")])
    email = models.EmailField(null=True, blank=True)

class Lab (models.Model) :
    name = models.CharField(primary_key=True, max_length=50) 
    end_point = models.URLField()
    api_key = models.TextField()
    

class BloodExpert (User) :
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

class TimeService (models.Model) :
    expert_snn = models.ForeignKey(BloodExpert, on_delete=models.CASCADE)
    date = models.DateField()
    stime = models.TimeField()
    etime = models.TimeField()
    evailable = models.BooleanField()
    

    class Meta : 
        unique_together = (("expert_snn", "date", "stime", "etime"))

    


