from django.shortcuts import render
import requests
from .models import *
import datetime

def starting(request):
    return render(request,"homepage.html")
def home(request):
    return render(request,"index.html")
def about(request):

        
    if request.method == "POST":
        user = request.POST.get("name")
        contact = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("message")
        fed = feedback(user = user,contact = contact, email=email, msg=desc)
        fed.save()
        return render(request, "about.html")
    



    return render(request,"about.html")
def market(request):
    return render(request,"market.html")

def charts(request):
    return render(request,"charts.html")
def news(request):
    return render(request,"news.html")
def analyse(request):
    return render(request,"beg.html")
def login(request):
    return render(request,"homepage.html")
def login1(request):
    try:
        if request.method == "POST":
            f_name = request.POST.get("fname")
            l_name = request.POST.get("lname")
            mail = request.POST.get("mail")
            psw = request.POST.get("psw")
            regist = reg(fname = f_name ,lname = l_name ,email=mail.lower(), password = psw,date  =datetime.datetime.today())
            if not reg.objects.filter(email=mail,password = psw):
                if [validate_email(mail)]:
                    regist.save()
                    return render(request,"login2.html")
            else:
                return render(request,'login1.html',{'value':0})
    except:
        html = {'value': 1}
        return render(request, "login2.html", html)
    return render(request,"login1.html")
def login2(request):
    if request.method == "POST":
        email = request.POST.get("email")
        psw = request.POST.get("psw")
        if not reg.objects.filter(email=email,password = psw):
            html = {'value':1}
            return render(request,"login2.html",html )
        else:
            return render(request,'login1.html')
    return render(request,"login2.html")
def tutorial(request):
    return render(request,"tutorial.html")
