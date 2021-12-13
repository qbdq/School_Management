from enum import unique
from django.db import models
from django.db.models import base
from django.db.models.expressions import F
from django.utils import timezone

# Create your models here.
dir = '../media'


# This class will be herited from
class Person(models.Model):
    nom = models.CharField(max_length=30, blank=False)
    prenom = models.CharField(max_length=30, blank=False)
    date_naissance = models.DateField(default=timezone.now)
    photo= models.ImageField(null=True,blank=True,upload_to=dir)
    adress_email = models.EmailField(max_length=70,blank=False)
    Added = models.DateField(default=timezone.now)

    class Meta:
        abstract = True


# La classe Module
class Module (models.Model): 
    # Module choices
    type_module = models.TextChoices('Obligatoire' ,'Optionnel')#adjust

    # Model attributes
    id_module = models.AutoField(primary_key=True)
    nom_module = models.CharField(max_length=30, blank=False, unique=True)
    nbr_heures_module = models.PositiveIntegerField(blank=False)
    type_module = models.CharField(max_length=2,choices=type_module.choices)
    niveau_etude = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table='module'


#######

class Groupe (models.Model) : 
    id_groupe = models.AutoField(primary_key=True)
    nom_groupe = models.CharField(max_length=10, blank=False)
    nombre_etudiant = models.PositiveIntegerField(max_length=40, blank=False)
    mail_groupe = models.EmailField(max_length=70,null=True,blank=True)
    niveau_etude = models.CharField(max_length=10, blank=False)
    module_groupe=models.ManyToManyField(Module) ## adjust table

    class Meta:
        db_table='Groupe'

 


class Travail_A_Rendre (models.Model):
    EtatTAF  = models.TextChoices('valide','non valide')#adjust

    id_taf = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50, blank=False)
    date_lancement = models.DateTimeField(default=timezone.now)
    date_lim_retour = models.DateTimeField(default=timezone.now)
    nature = models.CharField(max_length=50, blank=False)
    descriptif_taf = models.CharField(max_length=200, blank=False)
    pieces_enonce = models.FileField(upload_to=dir, max_length= 254) 
    pieces_rendu = models.FileField(upload_to=dir, max_length= 254) 
    etat_travail = models.CharField(max_length=10,choices=EtatTAF.choices)
    note = models.PositiveIntegerField(max_length=2, default=0, blank=True)
    commentaire = models.CharField(max_length=100, blank=False)
    id_module=models.ForeignKey(Module,on_delete=models.CASCADE)

    class Meta:
        db_table='travail_a_rendre'   





class Etudiant (Person) :
    id_etudiant = models.AutoField(primary_key=True)
    etat_etudiant = models.TextChoices('Abscent','Present','Retard','Exclu') #adjust
    situation_etudiant = models.TextChoices('Nouveau','Redoublant','Derogatrice','Autre')#adjust
    etat_etudiant = models.CharField(max_length=10,choices=etat_etudiant.choices)
    situation_etudiant = models.CharField(max_length=10,choices=situation_etudiant.choices)
    id_groupe=models.ForeignKey(Groupe,on_delete=models.CASCADE)
    travail_etud=models.ManyToManyField(Travail_A_Rendre) #Adjust

    class Meta:
        db_table='etudiant'


class Enseignant (Person) :
    id_enseignant = models.AutoField(primary_key=True)
    nbr_heure = models.PositiveIntegerField(max_length=2, blank=False)
    Modul_ensei=models.ManyToManyField(Module) # Adjust
    class Meta:
        db_table='enseignant'


class Seance (models.Model): 
    
    EtatSeance = models.TextChoices('Annulée','Différée','En cours','Términée')#adjust
    TypeSeance = models.TextChoices('Normal','Rattrapage','Soutien','Formation')#adjust

    id_seance = models.AutoField(primary_key=True)
    heure_debut = models.PositiveIntegerField(max_length=2, blank=False)
    heure_fin = models.PositiveIntegerField(max_length=2, blank=False)
    num_salle =  models.PositiveIntegerField(max_length=100, blank=False)
    objectif =  models.CharField(max_length=100, blank=True)
    resume = models.CharField(max_length=500, blank=True)
    etat_seance = models.CharField(max_length=6,choices=EtatSeance.choices)
    type_seance = models.CharField(max_length=2,choices=TypeSeance.choices)
    outils = models.CharField (max_length=100, blank=True)
    idModule=models.ForeignKey(Module,on_delete=models.CASCADE)

    class Meta:
        db_table='seance'    


   







class Enregistrement (models.Model): 
    TypeEnregistrement = models.TextChoices('mp4','flv','mov','avi','wmv')#adjust
    id_enreg = models.AutoField(primary_key=True)
    nom_enreg = models.CharField(max_length=100, blank=False, unique = True)
    url = models.URLField(max_length=100,blank=True)
    contenu_enreg =  models.URLField(max_length=100,blank=True)
    type_enreg = models.CharField(max_length=4,choices=TypeEnregistrement.choices) 
    desrcription_enreg = models.CharField(max_length=100, blank=True)
    date_enreg =  models.DateTimeField(default=timezone.now)
    id_seance=models.ForeignKey(Seance,on_delete=models.CASCADE)

    class Meta:
        db_table='enregistrement'

class Absence(models.Model):
    id_absence= models.AutoField(primary_key=True)
    date_absence= models.DateTimeField(default=timezone.now)
    motif=models.CharField(max_length=100, blank=True)
    justificatif=models.CharField(max_length=100, blank=True)
    id_etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    Abs_se= models.OneToOneField(
        Seance,
        on_delete=models.CASCADE,
        primary_key=True,
    ) # Adjust

    class Meta:
        db_table='absence'