from atexit import register
from django.conf import settings
from django.shortcuts import redirect,render
from .models import Author


# Create your views here.

def home(request):
    return render(request,'home.html')

def navbar(request):
    return render(request,'navbar.html')

def login(request):
    return render(request,'login.html')

def blog(request):
    aut=Author.objects.all()
    return render(request,'blog.html',{'aut':aut})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['name']
    y=request.POST['title']
    z=request.POST['description']
    
    image=request.POST['image']
    print(image)
    aut=Author(name=str(x),title=y,description=z, image =image)
    aut.save()
    return redirect("blog")

def delete(request,id):
    aut=Author.objects.get(id=id)
    aut.delete()
    return redirect("blog")

def update(request,id):
    aut=Author.objects.get(id=id)
    return render(request,'update.html',{'aut':aut})

def uprec(request,id):
    x=request.POST['name']
    y=request.POST['title']
    z=request.POST['description']
    aut=Author.objects.get(id=id)
    aut.name=x
    aut.title=y
    aut.description=z
    aut.save()
    return redirect("blog")
