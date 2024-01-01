from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render

def redirect_to_url(request):
    os = request.GET.get("os")
    code = request.GET.get("code")
    deeplink = f'unitydl://mylink?code={code}'
    
    # Redirect to the Unity3D link
    return render(request,'experiment.html',context={"deeplink":deeplink})