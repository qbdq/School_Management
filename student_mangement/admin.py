from django.contrib import admin
from .models import Etudiant , Enseignant , Module , Groupe , Seance
# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Enseignant)
admin.site.register(Module)
admin.site.register(Groupe)
admin.site.register(Seance)

