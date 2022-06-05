from django.contrib import admin
from .models import Order, Item, Payment, Event

# Register your models here.
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(Event)