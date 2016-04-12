# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login
from forms import loginForm


def index(request):
	form = loginForm(request.POST or None)	
	if form.is_valid():
		username = request.POST['username']
		password = request.POST['passsword']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home')
			else:
				return HttpResponse('Giriş Başarılı')

	title = "SosyoGündem Giriş"			
	context = {
		"form":form, 
		"pageName":title
	}

	template = "index.html"
	return render(request, template, context)



def dashboard(request):
	context = {}
	template = "dashboard.html"
	return render(request, template, context)

def mailListesi(request):
	context = {}
	template = "mail-listesi.html"
	return render(request, template, context)

def kullaniciListesi(request):
	context = {}
	template = "kullanici-listesi.html"
	return render(request, template, context)

def cikis(request):	
	return HttpResponseRedirect("/dashboard")

