from django.contrib import admin
from polls.models import UserProfile, OnemDerecesi, MailList, Gundem, User

# Register your models here.
class GundemAdmin(admin.ModelAdmin):		 
	search_fields = ('gundem_adi',)	
	list_display = ('gundem_adi', 'onem_derecesi', 'ekleyen_kullanici','get_tags',)

class MailListAdmin(admin.ModelAdmin):		 
	search_fields = ('user',)

class OnemDerecesiAdmin(admin.ModelAdmin):		 
	pass

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'telefon', 'tanim',)


admin.site.register(Gundem, GundemAdmin)
admin.site.register(MailList, MailListAdmin)
admin.site.register(OnemDerecesi, OnemDerecesiAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

