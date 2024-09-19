from django.contrib import admin
from fruits.models import Fruit

class FruitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'fresh', 'classification')
    search_fields = ('name',)
    
admin.site.register(Fruit, FruitsAdmin)