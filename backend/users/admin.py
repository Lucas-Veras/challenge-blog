from django.contrib import admin

# Register your models here.
from .models import User, Person

admin.site.register(User)
admin.site.register(Person)
