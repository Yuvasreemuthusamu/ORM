

from django.db import models
from django.contrib import admin
class Footballplayer (models.Model):
      name=models.CharField(max_length=15)
      weight=models.IntegerField()
      age=models.IntegerField()
      members=models.CharField(max_length=20)

class FootballplayerAdmin(admin.ModelAdmin):
    list_display=('name','weight','age','members')