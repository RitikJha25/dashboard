from django.db import models
import datetime

class Signup(models.Model):
	emailId = models.CharField(primary_key = True,max_length = 50,)
	password = models.CharField(max_length = 20)

def __str__():
	return self.emailId
	return self.password


# Create your models here.
class Temprature(models.Model):
	Tid = models.AutoField(primary_key = True, auto_created = True,)
	date = models.DateTimeField(auto_now_add = True, blank = True)
	temp = models.FloatField()


def __str__(self):
	return self.Tid
	return self.date
	return self.round(temp, 2)


class Tutorial(models.Model):
	date = models.DateTimeField(auto_now_add = True, blank = True)
	Timage = models.ImageField(upload_to = 'gallery/',)
	Reference = models.CharField(max_length = 100,)
	Title = models.CharField(max_length = 100,)


def __str__(self):
	return self.date
	return self.Title
	return self.Reference
	return self.name + ": " + str(self.Timage)


class Blogs(models.Model):
	Date = models.DateTimeField(auto_now_add = True, blank = True)
	Title = models.CharField(max_length = 100, )
	Description  = models.CharField(max_length = 10000)
	BlogImg = models.ImageField(upload_to = 'gallery/')


def __str__(self):
	return self.Date
	return self.Title
	return self.Description
	return self.name + ": " + str(self.BlogImg)