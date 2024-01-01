"""
URL configuration for SchoolChapter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from .views import topic,search_everything,mcq, mcq_submittion,fomcq_submittion
from .experiments import redirect_to_url

urlpatterns = [
    path('', topic),
    path('search/', search_everything),
    path('mcq/', mcq),
    path('mcq-submittion/', mcq_submittion),
    path('fomcq-submittion/', fomcq_submittion),
    path('exp/', redirect_to_url),
]
