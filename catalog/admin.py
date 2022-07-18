from catalog.models import City, Client, Commodity, Retailer

from django.contrib import admin


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'city')
    filter_vertical = ["commodity"]
    search_fields = ['first_name', 'last_name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('title', 'city')
