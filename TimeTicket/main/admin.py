from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.forms import TextInput, Textarea
from django.db import models


class ProductVideoAdmin(admin.ModelAdmin):
    pass


class ProductVideoInline(admin.StackedInline):
    model = ProductVideo


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVideoInline]


userfields = list(UserAdmin.fieldsets)
userfields[1] = ('Личная информация', {'fields': ('first_name', 'last_name', 'middle_name', 'email', 'mobilephone')})
UserAdmin.fieldsets = tuple(userfields)

admin.site.register(ProductVideo, ProductVideoAdmin)
admin.site.register(Event, ProductAdmin)
admin.site.register(NewUser, UserAdmin)
