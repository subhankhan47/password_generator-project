from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/home.html", {"password":"jri4nmf8jnfj"})
def eggs(request):
    return HttpResponse("eggs are tasty!")
def password(request):
    characters=list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('number'):
        characters.extend(list("0123456789"))
    if request.GET.get('special_characters'):
        characters.extend(list("!@#$%^&*()|?"))
    length=int(request.GET.get('length',10))
    thepassword=""
    for x in range(length):
        thepassword+=random.choice(characters)

    return render(request,"generator/password.html",{'password':thepassword})
