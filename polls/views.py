# -*- coding: utf-8 -*- 
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import loginForm
from models import *

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard/')

	form = loginForm(request.POST or None)
	title = "SosyoGündem Giriş"			
	context = {
		'form':form,
		"pageName":title
	}

	template = "index.html"

	return render(request, template, context)

def auth_view(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/dashboard/')		

			else:
				print 'disabled'
				return HttpResponseRedirect('/')
		else:
			form = loginForm(request.POST or None)
			title = "SosyoGündem Giriş"			
			hata = 'Kullanıcı Bulunamadı'
			context = {
				'hata':hata,
				'form':form,
				"pageName":title
			}

			template = "index.html"

			return render(request, template, context)

	#eğer sayfayı refresh ederse
	else:
		return HttpResponseRedirect('/')

		
@login_required
def dashboard(request):
	current_user = request.user
	gundem = Gundem.objects.all()
	onem = OnemDerecesi.objects.all()
	title = "SosyoGündem - %s" % current_user 			

	context = {
		'user':current_user,
		'gundem':gundem,
		'pageName':title,
		'onem_derecesi': onem
	
		
	}
	template = "dashboard.html"
	return render(request, template, context)

@login_required
def mailListesi(request):
	context = {}
	template = "mail-listesi.html"
	return render(request, template, context)

@login_required
def kullaniciListesi(request):
	context = {}
	template = "kullanici-listesi.html"
	return render(request, template, context)

def cikis(request):	
	logout(request)
	return HttpResponseRedirect("/")

