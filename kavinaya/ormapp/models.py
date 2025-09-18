from django.db import models
from django.contrib import admin
class Car(models.Model):
    mid=models.IntegerField()
    cname=models.CharField(max_length=100)
    collection=models.IntegerField()
    year=models.IntegerField()
    rating=models.FloatField()

class CarAdmin(admin.ModelAdmin):
    list_display=('mid','cname','collection','year','rating')


