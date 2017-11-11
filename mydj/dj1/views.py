from django.shortcuts import render
# Create your views here.
def index(request):
    connect={}
    connect['title']="打印"
    return render(request,"index.html",connect)