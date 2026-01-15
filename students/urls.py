from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_create, name='student_create'),
    path('list/', views.student_list, name='student_list'),
    path('', views.student_list, name='home'),
]
