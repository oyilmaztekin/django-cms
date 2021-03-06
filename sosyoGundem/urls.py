"""sosyoGundem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from polls import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^gundem/(?P<pk>[0-9]+)/$', login_required(views.GundemDetayView.as_view()), name='gundem-detay'),
    url(r'^gundem-create/', login_required(views.GundemCreate.as_view(success_url=('/dashboard'))),
        name='gundem-create'),
    url(r'^gundem-update/(?P<pk>[0-9]+)/$', login_required(views.GundemUpdate.as_view(success_url=('/dashboard'))), name='gundem-update'),
    url(r'^gundem-delete/(?P<pk>[0-9]+)/$', login_required(views.gundemDelete.as_view(success_url=('/dashboard'))),
        name='gundem-delete'),
    url(r'^gundem_check', views.gundem_check_view, name='gundem_check'),
    url(r'^mail-listesi/', views.mailListesi, name='mailListesi'),
    url(r'^kullanici-listesi/', views.kullaniciListesi, name='kullaniciListesi'),
    url(r'^cikis/', views.cikis, name='cikis'),
    url(r'^auth_view/', views.auth_view, name='auth_view'),
    url(r'^onem-create/', login_required(views.OnemCreate.as_view(success_url=('/dashboard'))),
        name='onem-create'),
    url(r'^mail-ekle/', login_required(views.MailCreate.as_view(success_url=('/dashboard'))),
        name='mail-create'),
    url(r'^kullanici-ekle/', login_required(views.UserCreate.as_view(success_url=('/dashboard'))),
        name='user-create'),
    
    
]