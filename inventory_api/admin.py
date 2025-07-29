from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'creation_date', 'update_date')
    list_filter = ('name',)
    search_fields = ('name', 'description')


admin.site.register(Menu, MenuAdmin)
