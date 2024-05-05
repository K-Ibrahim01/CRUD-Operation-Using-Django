from django.contrib import admin
from app.models import Person
class PersonModelAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Password')
admin.site.register(Person, PersonModelAdmin)