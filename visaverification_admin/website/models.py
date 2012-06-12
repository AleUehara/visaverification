from django.db import models

class User(models.Model):
   name      = models.CharField(max_length=200)
   email     = models.EmailField(max_length=100)

class Site(models.Model):
    name     = models.CharField(max_length=200)
    url      = models.CharField(max_length=2000)
    words    = models.CharField(max_length=2000)
    users     = models.ManyToManyField(User)

