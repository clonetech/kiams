from django.urls import path, include
from interns import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'interns'

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),

]
