from django.shortcuts import render, HttpResponse


def about_case(request):
    return HttpResponse('about_case')


def whyus_case(request):
    return HttpResponse('whyus_case')


def menu_case(request):
    return HttpResponse('menu_case')


def specials_case(request):
    return HttpResponse('specials_case')


def events_case(request):
    return HttpResponse('events_case')
