from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.dashboard,name='dashboard'),
    path('', views.test, name='test1'),
    path('connexion/',views.check_user,name='login'),
]