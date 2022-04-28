from curses.ascii import HT
from django.http import HttpResponse
from django.conf import settings


def AddedView(request):
    return HttpResponse("Hello World!")
