from django import forms
from django.contrib.auth.models import User
from . models import Posts
from . models import Category
from . models import Unwanted
#ghada
from . models import Comment

import re
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist


class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','email')

class Postform(forms.ModelForm):
    class Meta:
        model = Posts
        fields=('img','title','p_body','tag','cat_name',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'p_body': forms.TextInput(attrs={'class': 'form-control post_body'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Catform(forms.ModelForm):
    class Meta:
        model = Category
        fields=('category_name',)
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

            



class Wordform(forms.ModelForm):
    class Meta:
        model = Unwanted
        fields=('word',)


class RegistrationForm(UserCreationForm):

    username=forms.CharField(label='Username',max_length=30)
    email=forms.EmailField(label='Email')
    class Meta:
        model=User
        fields=('username','email',)

    def clean_username(self):
        username=self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('username is already taken.')

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('email is already taken.')
