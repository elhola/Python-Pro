from django.shortcuts import HttpResponse


def base(request):
    return HttpResponse('this is the first page in my site')
