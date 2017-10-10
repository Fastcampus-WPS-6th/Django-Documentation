from django.contrib import admin

from model.models.many_to_many import TwitterUser
from .models import Car, Manufacturer, User, Pizza, Topping

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(TwitterUser)
