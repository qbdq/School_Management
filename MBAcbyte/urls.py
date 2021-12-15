"""MBAcbyte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student_mangement import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('test/',views.showDemoPage,name ='test'),

    path('add_student/',views.add_student ,name='add_student'),
    path('add_enseignant/',views.add_enseignant ,name='add_enseignant'),
    path('add_seance/',views.add_seance ,name='add_seance'),
    path('add_groupe/',views.add_groupe ,name='add_groupe'),
    path('add_module/',views.add_module ,name='add_module'),


    path('manage_students/',views.manage_student,name='manage_students'),
    path('manage_enseignants/',views.manage_enseignants,name='manage_enseignants'),
    path('manage_groupes/',views.manage_groupes,name='manage_groupes'),
    path('manage_modules/',views.manage_modules,name='manage_modules'),
    path('manage_seances/',views.manage_seances,name='manage_seances'),

    path('edit_student/<int:student_id>', views.edit_student,name="edit_student"),
    path('edit_enseignant/<int:enseignant_id>', views.edit_enseignant,name="edit_enseignant"),
    path('edit_groupe/<int:groupe_id>', views.edit_groupe,name="edit_groupe"),
    path('edit_module/<int:module_id>', views.edit_module,name="edit_module"),
    path('edit_seance/<int:seance_id>', views.edit_seance,name="edit_seance"),



    path('add_student_save', views.add_student_save,name="add_student_save"),
    path('add_enseignant_save', views.add_student_save,name="add_enseignant_save"),
    path('add_seance_save', views.add_student_save,name="add_seance_save"),
    path('add_groupe_save', views.add_student_save,name="add_groupe_save"),
    path('add_module_save', views.add_student_save,name="add_module_save"),
    path('admin/', admin.site.urls)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)