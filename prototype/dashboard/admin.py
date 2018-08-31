from django.contrib import admin
from .models import Gym
# Register your models here.


class GymAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'number_of_people','capacity']


admin.site.register(Gym, GymAdmin)