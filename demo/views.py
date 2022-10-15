from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . import models
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .models import Temprature, Signup , Tutorial
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
import matplotlib.pyplot as plt

# Create your views here.
def Graphs(request):
	plt.plot([1,2,3,4],[1,4,9,16])
	plt.savefig('plot.jpg')	
	return render(request,'graphs.html',{'graphdata':'plot.jpg'})


def Main(request):
	webp_list= models.Temprature.objects.order_by('Tid')
	my_dict= {'web_list':webp_list,}
	return render(request,'dbrecord.html', context=my_dict)

def post_remove(request, id):
	if request.method == 'POST':
		rows = (models.Temprature.objects.order_by('Tid'))
		for r in rows:
			j = r.delete()
		return render(request,'signup.html',{'data':rows})

@ensure_csrf_cookie
@csrf_exempt
def SignupForm(request):
	if request.method == 'POST':
		if Signup.objects.filter(emailId = request.POST.get('emailId')).exists():
			user_exist= {'message': "User already exists "}
			return render(request,'signup.html', context = user_exist)

		if len(request.POST.get('password')) <= 8 and len(request.POST.get('password')) >=20:
			invalid_password= {'message' : "invalid password"}
			return render(request, 'signup.html',context = invalid_password)

		if request.POST.get('emailId') and request.POST.get('password'):
			post=Signup()
			post.emailId= request.POST.get('emailId')
			post.password= request.POST.get('password')
			post.save()
			success = {'message': "data uploaded successflly"}
			return render(request, 'signup.html', context= success)

	else:
		return render(request, 'signup.html', )


@ensure_csrf_cookie
@csrf_exempt
def LoginForm(request):
	if request.method == 'POST':
		if Signup.objects.filter(emailId = request.POST.get('emailId')).exists() and Signup.objects.filter(password = request.POST.get('password')).exists() :
			webp_list = models.Signup.objects.get(emailId = request.POST.get('emailId'))
			user_dict= {'user_list':webp_list,}
			return render(request,'project.html', context= user_dict)
		else:
			failed = {'message':"Invalid user or password"}
			return render(request, 'login.html',context = failed )

	else:
		return render(request,'login.html',)



def tutorial_data(request):
		webp_list= models.Tutorial.objects.order_by('date')
		my_dict= {'web_list':webp_list}
		return render(request,'project.html', context=my_dict)
		




def blogs_data(request):
		webp_list= models.Blogs.objects.order_by('Date')
		my_dict= {'web_list':webp_list}
		return render(request,'blogs.html', context=my_dict)
		