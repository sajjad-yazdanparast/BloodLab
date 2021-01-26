from django.db import models
from user.models import User, Lab
# Create your models here.

class TestType (models.Model) :
    name = models.CharField(primary_key=True, max_length=50) 
    lab = models.ManyToManyField('user.Lab')


class Order (models.Model) :
    TO_THE_WAY_OF_LAB = 0 #'tolab'
    PENDING_IN_LAB = 1 #'pending'
    READY_IN_LAB = 2 #'ready'
    TO_THE_WAY_OF_HOME = 3 #'tohome'
    CHOISES = (
        (TO_THE_WAY_OF_LAB,'Your order in the way to lab'),
        (PENDING_IN_LAB,'Your order is pending in lab'),
        (READY_IN_LAB,'Your order is ready in lab'),
        (TO_THE_WAY_OF_HOME,'Your order in the way to you'),
    )

    status = models.IntegerField(choices=CHOISES)
    price = models.FloatField()
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)



class Test(models.Model) :
    id = models.AutoField(primary_key=True, editable=False)
    type = models.ForeignKey(TestType, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null=True, related_name='tests')
    lab = models.ForeignKey('user.Lab', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('user.User', on_delete= models.CASCADE)
    result = models.TextField()
