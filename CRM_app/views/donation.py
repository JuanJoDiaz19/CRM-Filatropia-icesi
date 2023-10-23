from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from CRM_app.models import Donation,Allie

class donation_(View):
    def get(self, request, allie__id):
        
        try:
            donation_unsorted= Donation.objects.filter(allie_id= allie__id)
        except Donation.DoesNotExist:
            onation_unsorted= []
            
        try:
            ally = Allie.objects.get(id=allie__id)
        except Allie.DoesNotExist:
            ally = None
        
        total=0
        
        donation= sorted(donation_unsorted, key=lambda x: x.date, reverse=True)
        
        for i in donation_unsorted:
            total+=i.amount
            
        return render(request, 'allies/donation.html',{'donation':donation, 'allies': ally, 'total':total})