from django.db import models

class Town(models.Model):
    townName= models.CharField(max_length = 60)

    def __str__(self):
        return str(self.townName)

class Flat(models.Model):
    flatName = models.CharField(max_length =60)
    isAvailable= models.BooleanField(default=False)
    location = models.CharField(max_length = 60)

    def __str__(self):
        return str(self.flatName)

class Reserved(models.Model):
    beginDate = models.DateField()
    endDate = models.DateField()
    isFree = models.BooleanField(default=False)
    userName = models.CharField(max_length =60, default='Free')
    flatName = models.CharField(max_length = 60)
# Create your models here.
