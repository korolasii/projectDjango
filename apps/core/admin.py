from django.contrib import admin
from .models import *

class GamesAdmin(admin.ModelAdmin):
    search_fields = ['heros', 'cells', 'raritys']
    list_display = ['name_item',]
    list_filter = ['heros', 'cells', 'created_at', 'updated_at', 'raritys']
    prepopulated_fields = {'slug': ('name_item','price', 'quantity')}

class RaritysAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

class CellsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

class HerosAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Games, GamesAdmin)
admin.site.register(Raritys, RaritysAdmin)
admin.site.register(Cells, CellsAdmin)
admin.site.register(Heros, HerosAdmin)