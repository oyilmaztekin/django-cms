# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from forms import *
from models import *
from django.views.generic.detail import DetailView
from django.utils import timezone


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


class GundemDetayView(DetailView):

    queryset = Gundem.objects.all()
    template_name = "gundem-detay.html"

    def get_object(self):
        # Call the superclass
        gundem = super(GundemDetayView, self).get_object()
        # Record the last accessed date
        gundem.last_accessed = timezone.now()
        gundem.save()
        # Return the object
        return gundem

class GundemUpdate(UpdateView):
	"""template_name = "gundem-update.html"
	model = Gundem
	fields = '__all__'"""
	form_class = gundemForm
	model = Gundem
	template_name = "gundem-update.html"

	def form_valid(self, form):
		ekleyen_kullanici = self.request.user
		form.instance.ekleyen_kullanici = ekleyen_kullanici
		return super(GundemUpdate, self).form_valid(form)

	#fields = ('gundem_adi','tags','onem_derecesi','gundem_tarihi','gorusler')

class gundemDelete(DeleteView):
	model = Gundem
	template_name = "gundem-delete.html"

class GundemCreate(CreateView):
	model = Gundem
	form_class = gundemForm
	template_name = "gundem-create.html"

	def form_valid(self, form):
		ekleyen_kullanici = self.request.user
		form.instance.ekleyen_kullanici = ekleyen_kullanici
		return super(GundemCreate, self).form_valid(form)

class OnemCreate(CreateView):
	model = OnemDerecesi
	form_class = onemForm
	template_name = "onem-create.html"

	def form_valid(self, form):
		return super(OnemCreate, self).form_valid(form)


class MailCreate(CreateView):
	model = MailList
	form_class = mailForm
	template_name = "mail-create.html"

	def form_valid(self, form):
		return super(MailCreate, self).form_valid(form)

class UserCreate(CreateView):
	model = User
	form_class = userForm
	template_name = "kullanici-create.html"

	def form_valid(self, form):
		return super(UserCreate, self).form_valid(form)



#BURAYI YAPACAĞIZ
@login_required()
def gundem_check_view(FormView):
	Gundem.update()
	print "psd"


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

