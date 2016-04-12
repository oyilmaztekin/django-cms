# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

class loginForm(forms.ModelForm):
	username = forms.CharField(required=True,error_messages={'required':'kullanıcı adını boş bıraktınız'}, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Kullanıcı Adınız...'}),label = 'Email :')
	password = forms.CharField(required=True,error_messages={'required':'Şifreyi Boş Bıraktınız'}, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Şifreniz...'}),label = 'Email :')

	class Meta():
		model = User
		fields = '__all__'

