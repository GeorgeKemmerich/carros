from django.contrib import admin
from cars.models import Car, Brand


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'price')
    search_fields = ('model', 'model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)