from django.contrib import admin
from . import models
# Register your models here.
class contactUsAdmin(admin.ModelAdmin):
    list_display = ['fullname','email']
    list_editable = ['email']
admin.site.register(models.ContactUs, contactUsAdmin)