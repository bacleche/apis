from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def error_400(request, exception=None):
    return HttpResponse("Bad Request (400)", status=400)


def error_403(request, exception=None):
    return HttpResponse("Forbidden (403)", status=403)


def error_404(request, exception=None):
    return HttpResponse("Page not found (404)", status=404)


def error_500(request):
    return HttpResponse("Server error (500)", status=500)


