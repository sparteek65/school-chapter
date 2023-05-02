from django.shortcuts import render
from Dashboard.models import Topic
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from django.http import HttpResponseNotAllowed
from django.db.models import Q
import json
from Dashboard.models import McqOption,UserAnswer
# Create your views here.

def home(request):
    return render(request,'home.html',context={})