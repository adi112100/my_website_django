from django.shortcuts import render
from django.http import HttpResponse
from myprofile.models import Contact
from django.contrib import messages
from myprofile.information import lst
from myprofile.information import gamelinks
# Create your views here.


def index(request):
    return render(request, 'index.html')

def contactme(request):
    if request.method=='POST':
        firstname= request.POST.get("firstname")
        secondname=request.POST.get("lastname")
        email=request.POST.get("email")
        address1=request.POST.get("address1")
        address2=request.POST.get("address2")
        city=request.POST.get("city")
        zip=request.POST.get("zip")
        address = address1 + " " + address2
        
        contact = Contact(first_name=firstname, last_name=secondname, email=email, addr1=address, city=city, zipcode=zip)
        messages.success(request, 'Succesfully Received, Thanks For Contacting Us')
        
        contact.save()




    return render(request, 'contact.html')

def mlproject(request):

    context = {'data' : lst}
    return render(request, 'project.html', context)

def livegame(request):

    context = {'data' : gamelinks}
    return render(request, 'project1.html', context)

def game1(request):
    return render(request, 'game1.html')

def game2(request):
    return render(request, 'game2.html')

def game3(request):
    return render(request, 'game3.html')

def error(request):
    return HttpResponse("<h1>Sorry, Github Repo is private</h1>")