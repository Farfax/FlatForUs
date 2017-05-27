from django.contrib import admin
from .models import Town, Reserved, Flat

myModels = [ Town, Reserved, Flat ]
admin.site.register(myModels)
# Register your models here.
