from django.contrib import admin
from .models import *
from django.forms import TextInput, Textarea
from django.db import models


# class SpellcheckAdd(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'Spellcheck': 'true'})},
#     }


admin.site.register(Event),