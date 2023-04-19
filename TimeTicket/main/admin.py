from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.db import models


class ProductVideoAdmin(admin.ModelAdmin):
    pass


class ProductVideoInline(admin.StackedInline):
    model = ProductVideo


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVideoInline]


admin.site.register(ProductVideo, ProductVideoAdmin)
admin.site.register(Event, ProductAdmin)