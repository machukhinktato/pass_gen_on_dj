from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('generator/', views.gen_passwords, name='generator'),
    path('about/', views.about, name='about'),
]
