from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return (self.email_id)

class transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
     