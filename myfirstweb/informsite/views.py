from django.shortcuts import render
from django.http import HttpResponse
from .models import Notice

def home(request):
    return render(request, 'informsite/home.html')

def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'informsite/notice_list.html', {'notices': notices})