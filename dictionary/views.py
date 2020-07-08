from django.shortcuts import render,HttpResponse
from .models import semester
# Create your views here.
def home(request):
    semesters = semester.objects.all()
    return render(request,'dictionary/home.html',{'semesters':semesters})

def about(request):
    return render(request,"dictionary/about.html")

def contact(request):
    return render(request,"dictionary/contact.html")