from django import forms
from .models import Groupe

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
    """
    groupes = Groupe.get.all()
    groupe_list = []
    for groupe in groupes:
        item = (groupe.id_groupe,groupe.niveau_etude,groupe.nom_groupe)
        groupe_list.append(item)
    """

    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    date_naissance = forms.DateField(label="Date of birth",widget=DateInput(attrs={"class":"form-control"}))
    photo = forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))
    etat_etudiant = forms.ChoiceField(label="Course",choices=etat,widget=forms.Select(attrs={"class":"form-control"}))
    situation_etudiant = forms.ChoiceField(label="Course",choices=situation,widget=forms.Select(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    #groupe=forms.ChoiceField(label="Course",choices=groupe_list,widget=forms.Select(attrs={"class":"form-control"}))

class AddEnseignantForm(forms.Form):
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    date_naissance = forms.DateField(label="Date of birth",widget=DateInput(attrs={"class":"form-control"}))
    photo = forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))
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

    heure_debut = forms.DateTimeField(label="Heure Debut",widget=forms.DateTimeInput(attrs={"class":"form-control"}))
    heure_fin = forms.DateTimeField(label="Heure fin",widget=forms.DateTimeInput(attrs={"class":"form-control"}))
    num_salle = forms.CharField(label="Salle",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    objectif =  forms.CharField(label="Objectif",max_length=50,widget=forms.Textarea(attrs={"class":"form-control"}))
    resume =  forms.CharField(label="Resume",max_length=50,widget=forms.Textarea(attrs={"class":"form-control"}))
    etat_seance = forms.ChoiceField(label="Etat de seance ",choices=EtatSeance,widget=forms.Select(attrs={"class":"form-control"}))
    type_seance = forms.ChoiceField(label="Type de seance ",choices=TypeSeance,widget=forms.Select(attrs={"class":"form-control"}))
    outils =  forms.CharField(label="Outis",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    #idModule=models.ForeignKey(Module,on_delete=models.CASCADE)

class AddGroupeForm(forms.Form):
    name=forms.CharField(label="Nom du groupe",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    nombre_etudiant = forms.IntegerField(label="Nombre des etudiants",widget=forms.NumberInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    niveau_etude = forms.IntegerField(label="Nombre D'heure",widget=forms.NumberInput(attrs={"class":"form-control"}))

class AddModuleForm(forms.Form):
    Module_Choices = (
        ('Obligatoire','Obligatoire'),
        ('Optionnel','Optionnel')
    )
    name=forms.CharField(label="Nom du groupe",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    nbr_heure = forms.IntegerField(label="Nombre D'heure",widget=forms.NumberInput(attrs={"class":"form-control"}))
    niveau_etude = forms.CharField(label="Niveau D'étude",widget=forms.TextInput(attrs={"class":"form-control"}))
    type_module = forms.ChoiceField(label="Type Module",choices=Module_Choices,widget=forms.Select(attrs={"class":"form-control"}))


class EditStudentForm(forms.Form):
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

    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    date_naissance = forms.DateField(label="Date of birth",widget=DateInput(attrs={"class":"form-control"}))
    photo = forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))
    etat_etudiant = forms.ChoiceField(label="Course",choices=etat,widget=forms.Select(attrs={"class":"form-control"}))
    situation_etudiant = forms.ChoiceField(label="Course",choices=situation,widget=forms.Select(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    """
    courses=Courses.objects.all()
    course_list=[]
    for course in courses:
        small_course=(course.id,course.course_name)
        course_list.append(small_course)
    """
    