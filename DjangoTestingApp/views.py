from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Profile, JobExperience, SocialLink, Education, Skill, Workflow

def index(request):
    profile = Profile.objects.first()
    job_experiences = JobExperience.objects.all()
    social_links = SocialLink.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    workflows = Workflow.objects.all()
    
    context = {
        'profile': profile,
        'job_experiences': job_experiences,
        'social_links': social_links,
        'educations': educations,
        'skills': skills,
        'workflows': workflows
        }
    
    return render(request, 'DjangoTestingApp/index.html', context)
