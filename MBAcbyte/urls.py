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


    path('add_student_save', views.add_student_save,name="add_student_save"),
    path('add_enseignant_save', views.add_student_save,name="add_enseignant_save"),
    path('add_seance_save', views.add_student_save,name="add_seance_save"),
    path('add_groupe_save', views.add_student_save,name="add_groupe_save"),
    path('add_module_save', views.add_student_save,name="add_module_save"),

    path('admin/', admin.site.urls)

]