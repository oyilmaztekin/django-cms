# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
import datetime

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	telefon = models.CharField(verbose_name='Telefon', max_length=17)
	tanim = models.CharField(verbose_name="Tanım", max_length=150)
	slug = models.SlugField(unique=True)

	class Meta():
		verbose_name_plural = 'Kullanıcılar'

	def __unicode__(self):
		return '%s' % (self.first_name)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.username)

		return super(UserProfile, self).save(*args, **kwargs)

	def update(self, *args, **kwargs):
		#if not self.slug:
		self.slug = slugify(self.username)
		return super(UserProfile, self).save(*args, **kwargs)

class OnemDerecesi(models.Model):
	derece = models.CharField(verbose_name="Önem Derecesi", max_length=60)
	olusuturlma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True)
	slug = models.SlugField(unique=True)

	class Meta():
		verbose_name_plural = 'Önem Dereceleri'

	def __unicode__(self):
		return '%s' % (self.derece)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.derece)

		return super(OnemDerecesi, self).save(*args, **kwargs)

	def update(self, *args, **kwargs):
		#if not self.slug:
		self.slug = slugify(self.derece)

		return super(OnemDerecesi, self).save(*args, **kwargs)
        


class MailList(models.Model):
	user = models.ManyToManyField(User)
	olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True)
	slug = models.SlugField(unique=True)

	class Meta():
		verbose_name_plural = 'Mail Listesi'

	def __unicode__(self):
		return '%s' % (self.user)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.username)

		return super(MailList, self).save(*args, **kwargs)

	def update(self, *args, **kwargs):
		self.slug = slugify(self.username)


		return super(MailList, self).save(*args, **kwargs)
	
class Gundem(models.Model):
	gundem_adi = models.CharField(verbose_name="Gündemin Adı", max_length=200)
	olusturulma_tarihi = models.DateTimeField(editable=False, auto_now_add=True, null=True)
	gundem_tarihi = models.DateField(verbose_name="Gündemin Tarihi")
	onem_derecesi = models.ForeignKey(OnemDerecesi, on_delete=models.CASCADE)
	gorusler = models.TextField(verbose_name="Görüşler", max_length=255)
	ekleyen_kullanici = models.ForeignKey(User)
	tags = TaggableManager(verbose_name='Etiketler')
	slug = models.SlugField(unique=True, editable=False)

	class Meta():
		verbose_name_plural= 'Gündem Hadiseleri'

	def __unicode__(self):
		return '%s'  % (self.gundem_adi) + "\n"+", ".join([p.name for p in self.tags.all()])


	def get_tags(self):
		return "\n"+", ".join([p.name for p in self.tags.all()])

	def save(self, *args, **kwargs):
		self.slug = slugify(self.gundem_adi)
		self.olusturulma_tarihi = datetime.datetime.now()
		return super(Gundem, self).save(*args, **kwargs)

	def update(self, *args, **kwargs):
		self.slug = slugify(self.gundem_adi)
		self.olusturulma_tarihi = datetime.datetime.now()
		return super(Gundem, self).save(*args, **kwargs)



