from django.contrib import admin

from triangle.models import Log, Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    search_fields = ['first_name', 'last_name']


class LogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Log, LogAdmin)
admin.site.register(Person, PersonAdmin)
