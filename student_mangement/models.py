from enum import unique
from django.db import models
from django.db.models import base
from django.db.models.expressions import F
from django.utils import timezone

# Create your models here.


# This class will be herited from
class Person(models.Model):
    nom = models.CharField(max_length=30, blank=False)
    prenom = models.CharField(max_length=30, blank=False)
    date_naissance = models.DateField(default=timezone.now)
    photo= models.ImageField(null=True,blank=True)
    adress_email = models.EmailField(max_length=70,blank=False,unique=True)
    Added = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.nom + self.prenom
        
    class Meta:
        abstract = True


# La classe Module
class Module (models.Model): 
    # Module choices
    class Module_Choices (models.TextChoices):
        obligatoire = "Obligatoire"
        optionnel = "Optionnel"

    id_module = models.AutoField(primary_key=True)
    nom_module = models.CharField(max_length=30, blank=False, unique=True)
    nbr_heures_module = models.PositiveIntegerField(default=0, blank=False)
    type_module = models.CharField(max_length=20,choices=Module_Choices.choices , default = Module_Choices.obligatoire)
    niveau_etude = models.CharField(max_length=30, blank=False)

    def __str__(self) -> str:
        return str(self.id_module) + self.nom_module
    class Meta:
        db_table='module'


#######

class Groupe (models.Model) : 
    id_groupe = models.AutoField(primary_key=True)
    nom_groupe = models.CharField(max_length=100, blank=False)
    nombre_etudiant = models.PositiveIntegerField(default=0,blank=False)
    mail_groupe = models.EmailField(max_length=70,null=True,blank=True)
    niveau_etude = models.CharField(max_length=100, blank=False)
    module_groupe=models.ManyToManyField(Module , blank=True) # , through=  'id_module'  , through_fields =('','')

    def __str__(self) -> str:
        return str(self.id_groupe) +'-'+ self.nom_groupe
    class Meta:
        db_table='Groupe'

 






class Etudiant (Person) :
    id_etudiant = models.AutoField(primary_key=True)
    class etat_etudiants(models.TextChoices):
        Absence = 'Abscent' 
        Exclu = 'Exclu'
        Retard = 'Retard'
        Present = 'Present'
    class situation_etudiants(models.TextChoices):
        Nouveau = 'Nouveau'
        Redoublant = 'Redoublant'
        Derogatrice = 'Derogatrice'
        Autre = 'Autre'

    etat_etudiant = models.CharField(max_length=10,choices=etat_etudiants.choices)
    situation_etudiant = models.CharField(max_length=20,choices=situation_etudiants.choices)
    id_groupe=models.ForeignKey(Groupe,on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()
    
    class Meta:
        db_table='etudiant'


class Enseignant (Person) :
    id_enseignant = models.AutoField(primary_key=True)
    nbr_heure = models.PositiveIntegerField(default=0, blank=False)
    Modul_ensei=models.ManyToManyField(Module) #  , through=  'id_module'  , through_fields =('',''))  
    
    def __str__(self):
        return super().__str__()

    class Meta:
        db_table='enseignant'


class Seance (models.Model): 
    
    class EtatSeance(models.TextChoices) : 
        annule = 'Annulée'
        differe = 'Différée'
        en_cours = 'En cours'
        termine = 'Términée'
    class TypeSeance(models.TextChoices) : 
        Normal = 'Normal'
        Rattrapage = 'Rattrapage'
        Soutien = 'Soutien'
        Formation = 'Formation'

    id_seance = models.AutoField(primary_key=True)
    heure_debut = models.DateTimeField(default=timezone.now , blank=True)
    heure_fin = models.DateTimeField(default=timezone.now, blank=True)
    num_salle =  models.CharField(max_length=4, blank=False)
    objectif =  models.CharField(max_length=100, blank=True)
    resume = models.CharField(max_length=500, blank=True)
    etat_seance = models.CharField(max_length=10,choices=EtatSeance.choices)
    type_seance = models.CharField(max_length=10,choices=TypeSeance.choices)
    outils = models.CharField (max_length=100, blank=True)
    idModule=models.ForeignKey(Module,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id_seance) 
    class Meta:
        db_table='seance'    


   




class Travail_A_Rendre (models.Model):
    
    class EtatTAF (models.TextChoices):
        valid = "Valide"
        non_valid = "non valide"

    id_taf = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=50, blank=False)
    date_lancement = models.DateTimeField(default=timezone.now)
    date_lim_retour = models.DateTimeField(default=timezone.now)
    nature = models.CharField(max_length=50, blank=False)
    descriptif_taf = models.CharField(max_length=200, blank=False)
    pieces_enonce = models.FileField(max_length= 254) 
    pieces_rendu = models.FileField(max_length= 254) 
    etat_travail = models.CharField(max_length=10,choices=EtatTAF.choices , default=EtatTAF.valid)
    note = models.PositiveIntegerField(default=0, blank=True)
    commentaire = models.CharField(max_length=100, blank=False)
    id_module=models.ForeignKey(Module,on_delete=models.CASCADE)
    travail_etud=models.ManyToManyField(Etudiant) # , through=  'id_taf'  , through_fields =('','')

    def __str__(self) -> str:
            return self.id_taf + self.titre
   
    class Meta:
        db_table='travail_a_rendre'   




class Enregistrement (models.Model): 
    class TypeEnregistrement(models.TextChoices):
        mp4 = 'mp4'
        flv = 'flv'
        mov = 'mov'
        avi = 'avi'
        wmv = 'wmv'
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
    ) # Adjust

    class Meta:
        db_table='absence'


class Contact(models.Model):
    nom = models.CharField(max_length=30, blank=False)
    prenom = models.CharField(max_length=30, blank=False)
    adress_email = models.EmailField(max_length=70,blank=False,unique=True)
    say = models.CharField(max_length=500, blank=True)


