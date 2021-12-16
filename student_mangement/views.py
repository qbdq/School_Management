from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import Enseignant, Etudiant, Module, Seance
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
    return render(request,'manage_students_template.html',{"students":students})

def manage_enseignants(request):
    enseignants=Enseignant.objects.all()
    return render(request,'manage_enseignant_template.html',{"enseignants":enseignants})

def manage_groupes(request):
    groupes=Groupe.objects.all()
    return render(request,'manage_groupes_template.html',{"groupes":groupes})

def manage_modules(request):
    modules=Module.objects.all()
    return render(request,'manage_module_template.html',{"modules":modules})

def manage_seances(request):
    seances=Seance.objects.all()
    return render(request,'manage_seances_template.html',{"seances":seances})


def edit_student(request,student_id):
    request.session['student_id']=student_id
    student=Etudiant.objects.get(id_etudiant=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.adress_email
    form.fields['first_name'].initial=student.nom
    form.fields['last_name'].initial=student.prenom
    form.fields['etat_etudiant'].initial= student.etat_etudiant
    form.fields['situation_etudiant'].initial= student.situation_etudiant
    form.fields['date_naissance'].initial=student.date_naissance
    
    return render(request,"edit_student_template.html",{"form":form,"id":student_id})

def edit_student_save(request):
    pass


def edit_enseignant(request,enseignant_id):
    request.session['enseignant_id']=enseignant_id
    enseignant=Enseignant.objects.get(id_enseignant=enseignant_id)
    form=AddEnseignantForm()
    form.fields['email'].initial=enseignant.adress_email
    form.fields['first_name'].initial=enseignant.nom
    form.fields['last_name'].initial=enseignant.prenom
    form.fields['nbr_heure'].initial= enseignant.nbr_heure
    form.fields['date_naissance'].initial=enseignant.date_naissance
    return render(request,"edit_enseignant_template.html",{"form":form,"id":enseignant_id})

def edit_enseignant_save(request):
    pass


def edit_groupe(request,id_groupe):
    request.session['id_groupe']=id_groupe
    groupe=Groupe.objects.get(id_etudiant=id_groupe)
    form=AddGroupeForm()
    form.fields['name'].initial=groupe.nom_groupe
    form.fields['nombre_etudiant'].initial=groupe.nombre_etudiant
    form.fields['email'].initial=groupe.mail_groupe
    form.fields['niveau_etude'].initial= groupe.niveau_etude
    return render(request,"edit_groupe_template.html",{"form":form,"id":id_groupe})

def edit_groupe_save(request):
    pass


def edit_module(request,module_id):
    request.session['id_module']=module_id
    module=Module.objects.get(id_module=module_id)
    form=AddModuleForm()
    form.fields['name'].initial=module.nom_module
    form.fields['nbr_heure'].initial=module.nbr_heures_module
    form.fields['niveau_etude'].initial=module.niveau_etude
    form.fields['type_module'].initial= module.type_module
    return render(request,"edit_module_template.html",{"form":form,"id":module_id})

def edit_module_save(request):
    pass

def edit_seance(request,seance_id):
    request.session['seance_id']=seance_id
    seance=Seance.objects.get(id_seance=seance_id)
    form=AddSeanceForm()
    form.fields['heure_debut'].initial=seance.heure_debut
    form.fields['heure_fin'].initial=seance.heure_fin
    form.fields['num_salle'].initial=seance.num_salle
    form.fields['objectif'].initial= seance.objectif
    form.fields['resume'].initial= seance.resume
    form.fields['etat_seance'].initial= seance.etat_seance
    form.fields['type_seance'].initial= seance.type_seance
    form.fields['outils'].initial= seance.outils
    return render(request,"edit_seance_template.html",{"form":form,"id":seance_id})

def edit_seance_save(request):
    pass


def delete_enseignant(request,id_enseignant):
    pass