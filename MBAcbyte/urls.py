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
    path('test/',views.showDemoPage),
    path('add_student/',views.add_student ,name='test'),
    path('add_student_save', views.add_student_save,name="add_student_save"),


    path('admin/', admin.site.urls)

]