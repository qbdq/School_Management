from django.shortcuts import render
import requests
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import Etudiant
# Create your views here.

# test
def showDemoPage(request):
    return render(request,"demo.html")
def showStudentPage(request):
    return render(request,"student.html")   


def add_student_save(request):
    if request.method!="POST":
        return render(request, "404.html")
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
    
def add_enseignant_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddEnseignantForm(request.POST,request.FILES)
        if form.is_valid():
            pass
            try:
                messages.success(request,"Successfully Added xx")
            except:
                messages.error(request,"Failed to Add xxx")
        else:
            form=AddStudentForm(request.POST)
            return render(request, "add_enseignant_template.html", {"form": form})
    
def add_seance_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddSeanceForm(request.POST,request.FILES)
        if form.is_valid():
            pass
            try:
                messages.success(request,"Successfully Added xx")
            except:
                messages.error(request,"Failed to Add xxx")
        else:
            form=AddStudentForm(request.POST)
            return render(request, "add_enseignant_template.html", {"form": form})
   
def add_groupe_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddGroupeForm(request.POST,request.FILES)
        if form.is_valid():
            pass
            try:
                messages.success(request,"Successfully Added xx")
            except:
                messages.error(request,"Failed to Add xxx")
        else:
            form=AddStudentForm(request.POST)
            return render(request, "add_enseignant_template.html", {"form": form})
   
def add_module_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddModuleForm(request.POST,request.FILES)
        if form.is_valid():
            pass
            try:
                messages.success(request,"Successfully Added xx")
            except:
                messages.error(request,"Failed to Add xxx")
        else:
            form=AddStudentForm(request.POST)
            return render(request, "add_enseignant_template.html", {"form": form})
   


def add_student(request):
    form=AddStudentForm()
    return render(request,"add_student_template.html",{"form":form})

def add_enseignant(request):
    form=AddEnseignantForm()
    return render(request,"add_enseignant_template.html",{"form":form})

def add_seance(request):
    form = AddSeanceForm()
    return render(request,"add_seance_template.html",{"form":form})

def add_groupe(request):
    form = AddGroupeForm()
    return render(request,"add_groupe_template.html",{"form":form})

def add_module(request):
    form = AddModuleForm()
    return render(request,"add_module_template.html",{"form":form})



def manage_student(request):
    students=Etudiant.objects.all()
    for student in students:
        print(student.id_etudiant)

    return render(request,'manage_students_template.html',{"students":students})


def edit_student(request,student_id):
    request.session['student_id']=student_id
    student=Etudiant.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id.id
    form.fields['sex'].initial=student.gender
    form.fields['session_start'].initial=student.session_start_year
    form.fields['session_end'].initial=student.session_end_year
    return render(request,"edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})


def edit_student_save(request):
    pass