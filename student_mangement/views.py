from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .forms import *
from .models import Enseignant, Etudiant, Module, Person, Seance

from django.views.decorators.csrf import csrf_protect 

# Create your views here.

# test
def showDemoPage(request):
    return render(request,"home.html")


#homepage
def showStudentPage(request):
    return render(request,"home.html")   

def add_student_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            date_naissance=form.cleaned_data["date_naissance"]
            etat_etudiant=form.cleaned_data["etat_etudiant"]
            situation_etudiant=form.cleaned_data["situation_etudiant"]
            email=form.cleaned_data["email"]
            groupe=form.cleaned_data["groupe"]
            profile_pic=request.FILES['photo']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)
            profile_pic_url=profile_pic_url[len("media/"):]
            try :
                user=Etudiant()
                groupe = Groupe.objects.get(id_groupe=int(groupe))
                user.nom=first_name
                user.prenom=last_name
                user.date_naissance=date_naissance
                user.adress_email=email
                user.photo=profile_pic_url
                user.etat_etudiant=etat_etudiant
                user.situation_etudiant=situation_etudiant
                user.id_groupe=groupe
                user.save()
                messages.success(request,"Successfully Added Student {}".format(first_name))
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request,"Failed to Add Student {}".format(first_name))
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "add_student_template.html", {"form": form})
    
def add_enseignant_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddEnseignantForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            date_naissance=form.cleaned_data["date_naissance"]
            nbr_heure=form.cleaned_data["nbr_heure"]
            profile_pic=request.FILES['photo']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)
            profile_pic_url=profile_pic_url[len("media/"):]
            try:
                user=Enseignant()
                user.nom=first_name
                user.prenom=last_name
                user.date_naissance=date_naissance
                user.adress_email=email
                user.photo=profile_pic_url
                user.nbr_heure=nbr_heure
                user.save()
                messages.success(request,"Successfully Added Proffesor {}".format(first_name))
                return HttpResponseRedirect(reverse("add_enseignant"))
            except:
                messages.error(request,"Failed to Add Proffesor {}".format(first_name))
                return HttpResponseRedirect(reverse("add_enseignant"))
        else:
            form=AddEnseignantForm(request.POST)
            return render(request, "add_enseignant_template.html", {"form": form})
    
def add_seance_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddSeanceForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            heure_debut=form.cleaned_data["heure_debut"]
            heure_fin=form.cleaned_data["heure_fin"]
            num_salle=form.cleaned_data["num_salle"]
            objectif=form.cleaned_data["objectif"]
            resume=form.cleaned_data["resume"]
            etat_seance=form.cleaned_data["etat_seance"]
            type_seance=form.cleaned_data["type_seance"]
            outils=form.cleaned_data["outils"]
            module_id=form.cleaned_data["module"]
            module = Module.objects.get(id_module=int(module_id))
            try:
                seance=Seance()
                seance.heure_debut=heure_debut
                seance.heure_fin=heure_fin
                seance.num_salle=num_salle
                seance.objectif=objectif
                seance.resume=resume
                seance.etat_seance=etat_seance
                seance.type_seance=type_seance
                seance.outils=outils
                seance.idModule=module
                seance.save()
                messages.success(request,"Successfully Added session")
                return HttpResponseRedirect(reverse("add_seance"))
            except:
                messages.error(request,"Failed to Add session ")
                return HttpResponseRedirect(reverse("add_seance"))
        else:
            form=AddSeanceForm(request.POST)
            return render(request, "add_seance_template.html", {"form": form})

def add_groupe_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddGroupeForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data["name"]
            nombre_etudiant=form.cleaned_data["nombre_etudiant"]
            email=form.cleaned_data["email"]
            niveau_etude=form.cleaned_data["niveau_etude"]
            try:
                groupe= Groupe()
                groupe.nom_groupe=name
                groupe.nombre_etudiant=nombre_etudiant
                groupe.mail_groupe=email
                groupe.niveau_etude=niveau_etude
                groupe.save()
                messages.success(request,"Successfully Added Group {}".format(name))
                return HttpResponseRedirect(reverse("add_groupe"))
            except:
                messages.error(request,"Failed to Add  Groupe ")
                return HttpResponseRedirect(reverse("add_groupe"))
        else:
            form=AddGroupeForm(request.POST)
            return render(request, "add_groupe_template.html", {"form": form})

def add_module_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        form=AddModuleForm(request.POST,request.FILES)
        if form.is_valid():
            nom_module=form.cleaned_data["name"]
            nbr_heures_module=form.cleaned_data["nbr_heure"]
            type_module=form.cleaned_data["niveau_etude"]
            niveau_etude=form.cleaned_data["type_module"]
            try:
                module= Module()
                module.nom_module=nom_module
                module.nbr_heures_module=nbr_heures_module
                module.type_module=type_module
                module.niveau_etude=niveau_etude
                module.save()
                messages.success(request,"Successfully Added Module {}".format(nom_module))
                return HttpResponseRedirect(reverse("add_groupe"))
            except:
                messages.error(request,"Failed to Add  Module ")
                return HttpResponseRedirect(reverse("add_groupe"))
        else:
            form=AddModuleForm(request.POST)
            return render(request, "add_module_template.html", {"form": form})

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
    if request.method!="POST":
        return render(request, "404.html")
    else:
        student_id=request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(reverse("manage_students"))

        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            date_naissance=form.cleaned_data["date_naissance"]
            etat_etudiant=form.cleaned_data["etat_etudiant"]
            situation_etudiant=form.cleaned_data["situation_etudiant"]
            email=form.cleaned_data["email"]
            groupe=form.cleaned_data["groupe"]
            try :
                user=Etudiant.objects.get(id_etudiant=student_id)
                groupe = Groupe.objects.get(id_groupe=int(groupe))
                user.nom=first_name
                user.prenom=last_name
                user.date_naissance=date_naissance
                user.adress_email=email
                user.etat_etudiant=etat_etudiant
                user.situation_etudiant=situation_etudiant
                user.id_groupe=groupe
                user.save()
                messages.success(request,"Successfully edited Student {}".format(first_name))
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":user.id_etudiant}))
            except:
                messages.error(request,"Failed to Add to edit Student {}".format(first_name))
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        else:
            form=AddStudentForm(request.POST)
            return render(request, "edit_student_template.html", {"form": form})
    
def edit_enseignant(request,enseignant_id):
    request.session['enseignant_id']=enseignant_id
    enseignant=Enseignant.objects.get(id_enseignant=enseignant_id)
    form=EditEnsegiantForm()
    form.fields['email'].initial=enseignant.adress_email
    form.fields['first_name'].initial=enseignant.nom
    form.fields['last_name'].initial=enseignant.prenom
    form.fields['nbr_heure'].initial= enseignant.nbr_heure
    form.fields['date_naissance'].initial=enseignant.date_naissance
    return render(request,"edit_enseignant_template.html",{"form":form,"id":enseignant_id})

def edit_enseignant_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        enseignant_id=request.session.get("enseignant_id")
        if enseignant_id==None:
            return HttpResponseRedirect(reverse("manage_enseigiant"))
    form=EditEnsegiantForm(request.POST)
    if form.is_valid():
        first_name=form.cleaned_data["first_name"]
        last_name=form.cleaned_data["last_name"]
        date_naissance=form.cleaned_data["date_naissance"]
        email=form.cleaned_data["email"]
        nbr_heure=form.cleaned_data['nbr_heure']
        try :
            user=Enseignant.objects.get(id_enseignant=enseignant_id)
            user.nom=first_name
            user.prenom=last_name
            user.date_naissance=date_naissance
            user.adress_email=email
            user.nbr_heure=nbr_heure
            user.save()
            messages.success(request,"Successfully edited Proffesor {}".format(first_name))
            return HttpResponseRedirect(reverse("edit_enseignant",kwargs={"enseignant_id":user.id_enseignant}))
        except:
            messages.error(request,"Failed to Add to edit Proffesor {}".format(first_name))
            return HttpResponseRedirect(reverse("edit_enseignant",kwargs={"enseignant_id":user.id_enseignant}))
    else:
        form=AddStudentForm(request.POST)
        return render(request, "edit_ensegiant_template.html", {"form": form})

def edit_groupe(request,groupe_id):
    request.session['groupe_id']=groupe_id
    groupe=Groupe.objects.get(id_groupe=groupe_id)
    form=AddGroupeForm()
    form.fields['name'].initial=groupe.nom_groupe
    form.fields['nombre_etudiant'].initial=groupe.nombre_etudiant
    form.fields['email'].initial=groupe.mail_groupe
    form.fields['niveau_etude'].initial= groupe.niveau_etude
    return render(request,"edit_groupe_template.html",{"form":form,"id":groupe_id})

def edit_groupe_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        id_groupe=request.session.get("groupe_id")
        if id_groupe==None:
            return HttpResponseRedirect(reverse("manage_groupes"))
    form=AddGroupeForm(request.POST)
    if form.is_valid():
        nom_groupe=form.cleaned_data["name"]
        nombre_etudiant=form.cleaned_data["nombre_etudiant"]
        mail_groupe=form.cleaned_data["email"]
        niveau_etude=form.cleaned_data["niveau_etude"]
        try :
            groupe=Groupe.objects.get(id_groupe=id_groupe)
            groupe.nom_groupe=nom_groupe
            groupe.nombre_etudiant=nombre_etudiant
            groupe.mail_groupe=mail_groupe
            groupe.niveau_etude=niveau_etude
            groupe.save()
            messages.success(request,"Successfully edited groupe {}".format(nom_groupe))
            return HttpResponseRedirect(reverse("edit_groupe",kwargs={"groupe_id":id_groupe}))
        except:
            messages.error(request,"Failed to Add to edit Proffesor {}".format(nom_groupe))
            return HttpResponseRedirect(reverse("edit_groupe",kwargs={"groupe_id":id_groupe}))
    else:
        form=AddGroupeForm(request.POST)
        return render(request, "edit_groupe_template.html", {"form": form})


def edit_module(request,module_id):
    request.session['module_id']=module_id
    module=Module.objects.get(id_module=module_id)
    form=AddModuleForm()
    form.fields['name'].initial=module.nom_module
    form.fields['nbr_heure'].initial=module.nbr_heures_module
    form.fields['niveau_etude'].initial=module.niveau_etude
    form.fields['type_module'].initial= module.type_module
    return render(request,"edit_module_template.html",{"form":form,"id":module_id})

def edit_module_save(request):
    if request.method!="POST":
        return render(request, "404.html")
    else:
        module_id=request.session.get("module_id")
        if module_id==None:
            return HttpResponseRedirect(reverse("manage_modules"))
    form=AddModuleForm(request.POST)
    if form.is_valid():
        nom_module=form.cleaned_data["name"]
        nbr_heures_module=form.cleaned_data["nbr_heure"]
        type_module=form.cleaned_data["type_module"]
        niveau_etude=form.cleaned_data["niveau_etude"]
        try :
            module=Module.objects.get(id_module=module_id)
            module.nom_module=nom_module
            module.nbr_heures_module=nbr_heures_module
            module.type_module=type_module
            module.niveau_etude=niveau_etude
            module.save()
            messages.success(request,"Successfully edited module {}".format(nom_module))
            return HttpResponseRedirect(reverse("edit_module",kwargs={"module_id":module_id}))
        except:
            messages.error(request,"Failed to Add to edit Module {}".format(nom_module))
            return HttpResponseRedirect(reverse("edit_module",kwargs={"module_id":module_id}))
    else:
        form=AddModuleForm(request.POST)
        return render(request, "edit_module_template.html", {"form": form})

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
    if request.method!="POST":
        return render(request, "404.html")
    else:
        seance_id=request.session.get("seance_id")
        if seance_id==None:
            return HttpResponseRedirect(reverse("manage_seances"))
    form=AddSeanceForm(request.POST)
    if form.is_valid():
        heure_debut=form.cleaned_data["heure_debut"]
        heure_fin=form.cleaned_data["heure_fin"]
        num_salle=form.cleaned_data["num_salle"]
        objectif=form.cleaned_data["objectif"]
        resume=form.cleaned_data["resume"]
        etat_seance=form.cleaned_data["etat_seance"]
        type_seance=form.cleaned_data["type_seance"]
        outils=form.cleaned_data["outils"]
        idModule=form.cleaned_data["module"]
        try :
            seance=Seance.objects.get(id_seance=seance_id)
            module = Module.objects.get(id_module=int(idModule))
            seance.heure_debut=heure_debut
            seance.heure_fin=heure_fin
            seance.num_salle=num_salle
            seance.objectif=objectif
            seance.resume=resume
            seance.etat_seance=etat_seance
            seance.type_seance=type_seance
            seance.outils=outils
            seance.idModule=module
            seance.save()
            messages.success(request,"Successfully edited seance {}".format(seance_id))
            return HttpResponseRedirect(reverse("edit_seance",kwargs={"seance_id":seance_id}))
        except:
            messages.error(request,"Failed to Add to edit seance {}".format(seance_id))
            return HttpResponseRedirect(reverse("edit_seance",kwargs={"seance_id":seance_id}))
    else:
        form=AddSeanceForm(request.POST)
        return render(request, "edit_seance_template.html", {"form": form})



def delete_student(request,student_id):
    request.session['student_id']=student_id
    Etudiant.objects.filter(id_etudiant=student_id).delete()
    return redirect('/./manage_students/')

def delete_ensegiant(request,enseignant_id):
    request.session['enseignant_id']=enseignant_id
    Enseignant.objects.filter(id_enseignant=enseignant_id).delete()
    return redirect('/./manage_enseignants/')

def delete_groupe(request,groupe_id):
    request.session['groupe_id']=groupe_id
    Groupe.objects.filter(id_groupe=groupe_id).delete()
    return redirect('/./manage_groupes/')

def delete_module(request,module_id):
    request.session['module_id']=module_id
    Module.objects.filter(id_module=module_id).delete()
    return redirect('/./manage_modules/')

def delete_seance(request,seance_id):
    request.session['seance_id']=seance_id
    Seance.objects.filter(id_seance=seance_id).delete()
    return redirect('/./manage_seances/')



def search_student(request):
    if request.method == "POST":
        table_search = request.POST['table_search']
        students=Etudiant.objects.filter(nom__contains=table_search ,prenom__contains = table_search)
        return render(request,'manage_students_template.html',{"students":students})
    else:
        return render(request,'404.html')

    

def serach_ensegiant(request):
    if request.method == "POST":
        table_search = request.POST['table_search']
        enseignants=Enseignant.objects.filter(nom__contains=table_search ,prenom__contains = table_search)
        return render(request,'manage_enseignant_template.html',{"enseignants":enseignants})
    else:
        return render(request,'404.html')

def search_groupe(request):
    if request.method == "POST":
        table_search = request.POST['table_search']
        groupes=Groupe.objects.filter(nom_groupe__contains=table_search)
        return render(request,'manage_groupes_template.html',{"groupes":groupes})
    else:
        return render(request,'404.html')

def search_module(request):
    if request.method == "POST":
        table_search = request.POST['table_search']
        modules=Module.objects.filter(nom_module__contains=table_search)
        return render(request,'manage_module_template.html',{"modules":modules})
    else:
        return render(request,'404.html')


def search_seance(request):
    if request.method == "POST":
        table_search = request.POST['table_search']
        seances=Seance.objects.filter(num_salle__startswith=table_search)
        return render(request,'manage_seances_template.html',{"seances":seances})
    else:
        return render(request,'404.html')


def simple_stats(request):
    groupes = Groupe.objects.all()
    students = Etudiant.objects.all()
    enseignants=Enseignant.objects.all()
    modules=Module.objects.all()
    seances = Seance.objects.all()

    redoublant = 0
    new = 0
    derogataire = 0
    other = 0
    absence= 0
    Exclu= 0
    Retard= 0
    Present= 0
    for etudiant in students:
        if etudiant.situation_etudiant == 'Nouveau':
            new +=1
        elif etudiant.situation_etudiant == 'Redoublant':
            redoublant +=1
        elif etudiant.situation_etudiant == 'Derogatrice':
            derogataire +=1
        else:
            other+=1
        if etudiant.etat_etudiant =='Abscent':
            absence += 1
        elif etudiant.etat_etudiant =='Exclu':
            Exclu += 1   
        elif etudiant.etat_etudiant =='Retard':
            Retard += 1   
        elif etudiant.etat_etudiant =='Present':
            Present += 1    
    N_Etudiant = len(students)
    N_Groupe = len(groupes)
    N_Ensegiant = len(enseignants)
    N_Module = len(modules)
    N_Seance = len(seances)
    return render(request,'simple_stats.html',{"N_Etudiant":N_Etudiant,
    "N_Groupe":N_Groupe,
    "N_Ensegiant":N_Ensegiant,
    "N_Module":N_Module,
    "N_Seance":N_Seance,
    "redoublant":redoublant,
    "new":new,
    "derogataire":derogataire,
    "other":other,
    "Exclu":Exclu,
    "Present":Present,
    "absence":absence,
    "Retard":Retard,

    })


def advances_stats(request):

    return render(request,'advanced_stats.html')

def contact_us(request):
    form=AddContactForm()
    return render(request,'contact_us.html',{"form":form})

def team(request):
    
    return render(request,'team.html')
