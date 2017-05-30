from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date

class Town(models.Model):
    townName= models.CharField(max_length = 60)

    def __str__(self):
        return str(self.townName)

class Flat(models.Model):
    flatName = models.CharField(max_length =60, unique=True)
    canRent= models.BooleanField(default=True)
    location = models.ForeignKey(Town, default=1)
    openTime = models.DateField(default=date.today())
    openTimeEnd = models.DateField(default=date.today())
    #reservedDate = models.ManyToManyField('Reserved')

    def __str__(self):
        return str(self.flatName)

class Reserved(models.Model):
    beginDate = models.DateField(default=date.today())
    endDate = models.DateField(default=date.today())
    isFree = models.BooleanField(default=True)
    userName = models.CharField(max_length =60, default='Free')
    flatName = models.ForeignKey('Flat', default=1)

    def __str__(self):
        return 'From '+str(self.beginDate)+' to '+str(self.endDate)+' : '+str(self.userName)

    def save(self, *args, **kwargs):
        if(self.beginDate > self.endDate):
            raise ValidationError('Begin date cannot be bigger then end Date.')
        else:
            return super(Reserved, self).save(*args, **kwargs)
# Create your models here.
