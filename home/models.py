from django.db import models

# Create your models here.

class Clogin(models.Model):
    cid = models.CharField(max_length=10)
    Password = models.CharField(max_length=50)
    cname = models.CharField(max_length=120)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    nba_aggregated = models.CharField(max_length=5)
    duration_of_nba_aggregration = models.CharField(max_length=5 ,null=True)

    def __str__(self):
        return self.cname
    