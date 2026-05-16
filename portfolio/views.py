from django.shortcuts import render
from .models import Skill, Internship, Project

def index(request):
    skills = Skill.objects.all()
    internships = Internship.objects.all().order_by('-id')
    projects = Project.objects.all()

    context = {
        'skills': skills,
        'internships': internships,
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)
