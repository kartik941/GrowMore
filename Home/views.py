from django.shortcuts import render
import requests


def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def market(request):
    return render(request,"market.html")

def charts(request):
    return render(request,"charts.html")
