from django.db import models

# Create your models here.


class Student_Details(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class College_Details(models.Model):
    State = models.CharField(max_length=30)
    Cname = models.CharField(max_length=50)
    Ranking = models.CharField(max_length=3)
    sfratio = models.CharField(max_length=10)
    highestPackage = models.CharField(max_length=6)
    placementRatio = models.CharField(max_length=20)
    averagePackage = models.CharField(max_length=6)

    def __str__(self):
        return self.Cname
    
    