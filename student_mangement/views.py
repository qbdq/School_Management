from django.shortcuts import render
import requests
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .forms import AddStudentForm
from .models import Etudiant
# Create your views here.


def showDemoPage(request):
    return render(request,"demo.html")

def showStudentPage(request):
    return render(request,"student.html")   


def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        print('test')
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            date_naissance=form.cleaned_data["date_naissance"]
            email=form.cleaned_data["email"]
            course_id=form.cleaned_data["groupe.id_groupe"]
            etat_etudiant = form.cleaned_data["etat_etudiant"]
            situation_etudiant = form.cleaned_data["situation_etudiant"] 
            photo=request.FILES['photo']
            fs=FileSystemStorage()
            filename=fs.save(photo.name,photo)
            profile_pic_url=fs.url(filename)
            try:

                messages.success(request,"Successfully Added Student")
            except:
                messages.error(request,"Failed to Add Student")
        else:
            form=AddStudentForm(request.POST)
            return render(request, "add_student_template.html", {"form": form})
    
def add_student(request):
    form=AddStudentForm()
    return render(request,"add_student_template.html",{"form":form})
