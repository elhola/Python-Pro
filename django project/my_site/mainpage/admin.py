from django.contrib import admin
from .models import Dish, Category, Gallery

# Register your models here.
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Gallery)
