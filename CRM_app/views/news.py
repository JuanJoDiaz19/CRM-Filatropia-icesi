from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models.New import New

class News(View):
    def get(self, request):
        news = New.objects.all()  # Obtener todas las instancias de New
        return render(request, 'news.html', {'news': news})