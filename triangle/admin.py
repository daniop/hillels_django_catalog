from django.contrib import admin

from triangle.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    search_fields = ['first_name', 'last_name']


admin.site.register(Person, PersonAdmin)
