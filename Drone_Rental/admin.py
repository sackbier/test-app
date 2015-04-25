from django.contrib import admin

from .models import Drone, Customer, Case

admin.site.register(Drone)
admin.site.register(Customer)
admin.site.register(Case)