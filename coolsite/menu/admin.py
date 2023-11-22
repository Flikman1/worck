# menu/admin.py
from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')


admin.site.register(MenuItem, MenuItemAdmin)

# Register your models here.
