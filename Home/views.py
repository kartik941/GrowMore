from django.shortcuts import render
import requests
from .models import *


def home(request):
    return render(request,"index.html")
def about(request):

        
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("message")
        fed = feedback(name=name,phone = phone, email=email, msg=desc)
        if [validate_email(email)]:
            fed.save()
            return render(request, "about.html")
        else:
            html = {'value':1}
            return render(request, "about.html",)
    



    return render(request,"about.html")
def market(request):
    return render(request,"market.html")

def charts(request):
    return render(request,"charts.html")
def news(request):
    return render(request,"news.html")
def analyse(request):
    return render(request,"beg.html")
