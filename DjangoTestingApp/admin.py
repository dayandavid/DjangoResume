from django.contrib import admin

from .models import JobExperience
from .models import JobPosition

admin.site.register(JobExperience)
admin.site.register(JobPosition)
