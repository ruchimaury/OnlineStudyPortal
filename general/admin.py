from django.contrib import admin
from general .models import SigninModel,contactModel,myregModel
# Register your models here.
x=[ SigninModel,contactModel,myregModel]
for i in x:
    admin.site.register(i)

