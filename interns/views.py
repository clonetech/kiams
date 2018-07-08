from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone



def dashboard(request):

        template_name = 'dashboard.html'

        return render(request, 'dashboard.html')

def home(request):

        template_name = 'home.html'

        return render(request, 'home.html')
