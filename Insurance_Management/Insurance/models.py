from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Phone_number=models.IntegerField()
    Address=models.CharField(max_length=10,null=True)

def __str__(self):
    return self.user.username

class Ajents(models.Model):
    address = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True)
    Phone=models.IntegerField(null=True)
    start_Time = models.CharField(max_length=20,null=True)
    end_Time = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name
