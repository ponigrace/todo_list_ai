from django.urls import path
from . import views

urlpatterns = ([
    path('', views.home, name='home'),
    path('todo/new/', views.create_todo, name='create_todo'),
])


