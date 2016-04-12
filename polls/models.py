# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	telefon = models.CharField(verbose_name='Telefon', max_length=17)
	tanim = models.CharField(verbose_name="Tanım", max_length=150)
	class Meta():
		verbose_name_plural = 'Kullanıcılar'

	def __unicode__(self):
		return '%s' % (self.first_name)

class OnemDerecesi(models.Model):
	derece = models.CharField(verbose_name="Önem Derecesi", max_length=60)
	olusuturlma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True)
	class Meta():
		verbose_name_plural = 'Önem Dereceleri'

	def __unicode__(self):
		return '%s' % (self.derece)

class MailList(models.Model):
	user = models.ManyToManyField(User)
	olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True)

	class Meta():
		verbose_name_plural = 'Mail Listesi'

	def __unicode__(self):
		return '%s' % (self.user)
	
class Gundem(models.Model):
	gundem_adi = models.CharField(verbose_name="Gündemin Adı", max_length=200)
	olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True)
	gundem_tarihi = models.DateField(verbose_name="Gündemin Tarihi")
	onem_derecesi = models.ForeignKey(OnemDerecesi, on_delete=models.CASCADE)
	gorusler = models.TextField(verbose_name="Görüşler", max_length=255)
	ekleyen_kullanici = models.ForeignKey(User)
	tags = TaggableManager(verbose_name='Etiketler')
	class Meta():
		verbose_name_plural= 'Gündem Hadiseleri'

	def __unicode__(self):
		return '%s' % (self.gundem_adi)

	def get_tags(self):
		return "\n"+", ".join([p.name for p in self.tags.all()])
         



