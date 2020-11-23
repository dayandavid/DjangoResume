from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Profile, JobExperience, SocialLink

def index(request):
    profile = Profile.objects.first()
    job_experiences = JobExperience.objects.all()
    social_links = SocialLink.objects.all()
    
    context = {
        'profile': profile,
        'job_experiences': job_experiences,
        'social_links': social_links
        }
    
    return render(request, 'DjangoTestingApp/index.html', context)
