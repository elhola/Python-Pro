from django.shortcuts import render, HttpResponse
from .models import Category, Dish, Gallery
from .forms import UserReservationsForm
import random

def mainpage_view(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True).filter(is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True).filter(is_special=True)
    gallery = Gallery.objects.filter(is_visible=True)
    gallery = random.choices(gallery, k=8)
    user_reservation = UserReservationsForm()

    return render(request, 'mainpage.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'gallery': gallery,
        'form_reservation': user_reservation,
    })

