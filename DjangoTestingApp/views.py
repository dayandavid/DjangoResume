from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Profile, JobExperience, SocialLink

def index(request):
    profile = Profile.objects.first()
    jobExperiences = JobExperience.objects.all()
    social_links = SocialLink.objects.all()
    
    context = {
        'profile': profile,
        'job_experiences': jobExperiences,
        'social_links': social_links
        }
    
    return render(request, 'DjangoTestingApp/index.html', context)
