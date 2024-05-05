from django.db import models
class Person(models.Model):
    Name = models.CharField(max_length=30 ,null='false' ,blank='false' )
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)