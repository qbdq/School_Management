from django import forms
from .models import Groupe, Module

class DateInput(forms.DateInput):
    input_type = "date"



class AddStudentForm(forms.Form):

    etat = (
        ('Abscent','Abscent'),
        ('Exclu','Exclu'),
        ('Retard','Retard'),
        ('Present','Present'),
    )

    situation = (
        ('Nouveau','Nouveau'),
        ('Redoublant','Redoublant'),
        ('Derogatrice','Derogatrice'),
        ('Autre','Autre'),
    )


    groupes = Groupe.objects.all()
    groupe_list=[(q.id_groupe,q.nom_groupe)for q in groupes]
    

    

    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    date_naissance = forms.DateField(label="Date of birth",widget=DateInput(attrs={"class":"form-control"}))
    photo = forms.FileField(label="Profile Pic",max_length=100,widget=forms.FileInput(attrs={"class":"form-control"}))
    etat_etudiant = forms.ChoiceField(label="Course",choices=etat,widget=forms.Select(attrs={"class":"form-control"}))
    situation_etudiant = forms.ChoiceField(label="Course",choices=situation,widget=forms.Select(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    groupe=forms.ChoiceField(label="Groupes",choices=groupe_list,widget=forms.Select(attrs={"class":"form-control"}))

class AddEnseignantForm(forms.Form):
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    date_naissance = forms.DateField(label="Date of birth",widget=DateInput(attrs={"class":"form-control"}))
    photo = forms.FileField(label="Profile Pic",max_length=100,widget=forms.FileInput(attrs={"class":"form-control"}))
    nbr_heure = forms.IntegerField(label="Nombre D'heure",widget=forms.NumberInput(attrs={"class":"form-control"}))

class AddSeanceForm(forms.Form):
    EtatSeance=  (
        ('Annulée','Annulée'),
        ('Différée','Différée'),
        ('En cours','En cours'),
        ('Términée','Términée')
    )

    TypeSeance=  (
        ('Normal','Normal'),
        ('Rattrapage','Rattrapage'),
        ('Soutien','Soutien'),
        ('Formation','Formation')
    )

    heure_debut = forms.DateField(label="Heure Debut",widget=forms.DateInput(attrs={"class":"form-control"}))
    heure_fin = forms.DateField(label="Heure fin",widget=forms.DateInput(attrs={"class":"form-control"}))
    num_salle = forms.CharField(label="Salle",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    objectif =  forms.CharField(label="Objectif",max_length=50,widget=forms.Textarea(attrs={"class":"form-control"}))
    resume =  forms.CharField(label="Resume",max_length=50,widget=forms.Textarea(attrs={"class":"form-control"}))
    etat_seance = forms.ChoiceField(label="Etat de seance ",choices=EtatSeance,widget=forms.Select(attrs={"class":"form-control"}))
    type_seance = forms.ChoiceField(label="Type de seance ",choices=TypeSeance,widget=forms.Select(attrs={"class":"form-control"}))
    outils =  forms.CharField(label="Outis",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    modules = Module.objects.all()
    module_choice=[(q.id_module,q.nom_module)for q in modules]
    module=forms.ChoiceField(label="Module",choices=module_choice,widget=forms.Select(attrs={"class":"form-control"}))

    
    #idModule=models.ForeignKey(Module,on_delete=models.CASCADE)

class AddGroupeForm(forms.Form):
    name=forms.CharField(label="Nom du groupe",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    nombre_etudiant = forms.IntegerField(label="Nombre des etudiants",widget=forms.NumberInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    niveau_etude = forms.CharField(label="Niveau d'étude ",widget=forms.TextInput(attrs={"class":"form-control"}))



class AddModuleForm(forms.Form):
    Module_Choices = (
        ('Obligatoire','Obligatoire'),
        ('Optionnel','Optionnel')
    )
    name=forms.CharField(label="Nom du groupe",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    nbr_heure = forms.IntegerField(label="Nombre D'heure",widget=forms.NumberInput(attrs={"class":"form-control"}))
    niveau_etude = forms.CharField(label="Niveau D'étude",widget=forms.TextInput(attrs={"class":"form-control"}))
    type_module = forms.ChoiceField(label="Type Module",choices=Module_Choices,widget=forms.Select(attrs={"class":"form-control"}))


    