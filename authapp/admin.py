from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(usermodel)
class user(admin.ModelAdmin):
    list_display = ['id','user','phno']
    list_display_links = ['id','user','phno']
