from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import *

# Create your views here.

def signUp(request):
	user_form=RegistrationForm()
	if request.method=="POST":
		user_form=RegistrationForm(request.POST)
		if user_form.is_valid():
			user=User.objects.create(username=user_form.cleaned_data['username'],password=user_form.cleaned_data['password'],email=user_form.cleaned_data['email'])
			#user.save()
			return HttpResponseRedirect("/socialapp/signup/")
	context={"form":user_form}
	return render(request,"user/new.html",context)
