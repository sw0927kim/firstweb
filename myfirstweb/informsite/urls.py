from django.urls import path, include
from . import views

app_name='informsite'
urlpatterns = [
    
    path('', views.home, name='home'),
    path('notices/', views.notice_list, name='notice_list'),
]

