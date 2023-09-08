from django.shortcuts import redirect,render
from .models import Author


# Create your views here.

def home(request):
    return render(request,'home.html',context={
        "Name":"ShankarDev",
        "Location":"Putalisadak",
    })

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    aut=Author.objects.all()
    return render(request,'blog.html',{'aut':aut})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['second']
    z=request.POST['third']
    
    image=request.POST['image']
    print(image)
    mem=Author(name=str(x),title=y,description=z, image =image)
    mem.save()
    return redirect("blog")

def delete(request,id):
    aut=Author.objects.get(id=id)
    aut.delete()
    return redirect("blog")