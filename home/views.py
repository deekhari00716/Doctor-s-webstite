from django.shortcuts import render
from .models import Project, Profile_Pic

def home(request):
    projects = Project.objects.order_by('-date')
    profilepic = Profile_Pic.objects.all()
    return render(request, 'home/home.html',{'projects':projects,
    'profilepic':profilepic,
    })
