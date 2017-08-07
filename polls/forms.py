# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.auth.models import User
from polls.models import *
from django.utils import timezone
from django.utils.text import slugify
from taggit.forms import TagWidget, TagField

class loginForm(forms.ModelForm):
	username = forms.CharField(required=True,error_messages={'required':'kullanıcı adını boş bıraktınız'}, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Kullanıcı Adınız...'}),label = 'Email :')
	password = forms.CharField(required=True,error_messages={'required':'Şifreyi Boş Bıraktınız'}, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Şifreniz...'}),label = 'Email :')

	class Meta():
		model = User
		fields = '__all__'

class gundemForm(forms.ModelForm):
	gundem_adi = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),label='Gündem Adı :')
	gundem_tarihi = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control','placeholder':'12/12/2016'}),label='Gündem Tarihi:')
	onem_derecesi = forms.ModelChoiceField(required=True, queryset=OnemDerecesi.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label='Önem Derecesi:')
	gorusler= forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}),label='Görüşleriniz:')
	ekleyen_kullanici = forms.IntegerField(required=False, widget=forms.HiddenInput())
	tags = TagField(required=False, label="Etiketler", widget=TagWidget(attrs={'class':'form-control'}))


	class Meta():
		exclude = ["ekleyen_kullanici"]
		model = Gundem
		fields = '__all__'

class onemForm(forms.ModelForm):
	derece = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),label='Önem Derecesi :')

	class Meta():
		exclude = ["ekleyen_kullanici"]
		model = OnemDerecesi
		fields = '__all__'

class mailForm(forms.ModelForm):
	onem_derecesi = forms.ModelChoiceField(required=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label='Kullanıcı Seçin:')

	class Meta():
		exclude = ["ekleyen_kullanici"]
		model = MailList
		fields = '__all__'


class userForm(forms.ModelForm):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),label='Kullanıcı Adı :')
	first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),label='Adı :')
	last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),label='Soyadı :')
	email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),label='Mail Adresi :')
	class Meta():
		model = User
		fields = ['username','first_name', 'last_name', 'email']


