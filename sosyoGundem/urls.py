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

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^gundem/(?P<pk>[0-9]+)/$', views.GundemDetayView.as_view(), name='gundem-detay'),
    url(r'^mail-listesi/', views.mailListesi, name='mailListesi'),
    url(r'^kullanici-listesi/', views.kullaniciListesi, name='kullaniciListesi'),
    url(r'^cikis/', views.cikis, name='cikis'),
    url(r'^auth_view/', views.auth_view, name='auth_view'),
    
    
]
