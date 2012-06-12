from django.db import models

class User(models.Model):
   name      = models.CharField(max_length=200)
   email     = models.EmailField(max_length=100)
   def __unicode__(self):
   	return self.name

class CorporateEmail(models.Model):
	address     = models.EmailField(max_length=100)
	stmp_server = models.CharField(max_length=200)
	port        = models.IntegerField(max_length=5)
	password    = models.CharField(max_length=50)
	def __unicode__(self):
		return self.address

class Site(models.Model):
    name            = models.CharField(max_length=200)
    url             = models.URLField(max_length=2000)
    words           = models.CharField(max_length=2000)
    users           = models.ManyToManyField(User)
    corporate_email = models.ForeignKey(CorporateEmail)
    def __unicode__(self):
    	return self.name

