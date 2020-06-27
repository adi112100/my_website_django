from django.shortcuts import render
from django.http import HttpResponse
from myprofile.models import Contact
from django.contrib import messages
from myprofile.information import lst
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