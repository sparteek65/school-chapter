import random
import string
import urllib.parse as urlparse

import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request,'home.html',context={})


def logout_view(request):
    logout(request)
    return redirect('/')


def google_login(request):
    state = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    params = {
        'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        'response_type': 'code',
        'scope': 'email profile',
        'redirect_uri': request.build_absolute_uri('/')[:-1]+settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL,
        'state': state,
    }
    url = 'https://accounts.google.com/o/oauth2/auth?' + urlparse.urlencode(params)
    # request.session['google_oauth2_state'] = state
    return HttpResponseRedirect(url)


def google_callback(request):
    state = request.GET.get('state')
    code = request.GET.get('code')
    # if state != request.session.get('google_oauth2_state'):
    #     return HttpResponseRedirect('/login/')
    params = {
        'code': code,
        'client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        'client_secret': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        'redirect_uri': request.build_absolute_uri('/')[:-1]+settings.SOCIAL_AUTH_LOGIN_REDIRECT_URL,
        'grant_type': 'authorization_code',
    }
    response = requests.post('https://accounts.google.com/o/oauth2/token', data=params)
    token_data = response.json()
    headers = {'Authorization': 'Bearer ' + token_data['access_token']}
    params = {
    'personFields': 'names,emailAddresses,photos'
    }
    response = requests.get('https://people.googleapis.com/v1/people/me', headers=headers,params=params)
    user_data = response.json()
    email = user_data['emailAddresses'][0]['value']
    name = user_data['names'][0]["displayName"]
    password=settings.SECRET_KEY+email
    username=email.split("@")[0]
    try:
        user = User.objects.get(username=username)
        # user = authenticate(request, username=username, password=password, first_name=name)
    except User.DoesNotExist:
        user=User.objects.create_user(username=username, 
                                              email=email, 
                                              password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')
