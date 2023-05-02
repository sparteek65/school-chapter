from django.http import HttpResponseNotFound
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def dashboard(reqest):
    return render(reqest,'home.html')


def handler404(request, exception):
    return HttpResponseNotFound(render(request, '404.html'))
