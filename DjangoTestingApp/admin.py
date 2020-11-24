from django.contrib import admin

from .models import JobExperience, JobPosition, SocialLink, Profile, Education

admin.site.register(JobPosition)

class SocialLinkInline(admin.TabularInline):
    model = SocialLink


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User Description', {
            "fields": (
                ['first_name', 'last_name','description', 'interest','profile_pic']
            ),
        }),
        ('Personal Information', {
            "fields": (
                ['address', 'phone_number', 'email']
            ),
        }),
    )
    inlines = [SocialLinkInline]
    list_display = ('first_name', 'last_name', 'email')


@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                ['company_name', 'company_description', 'job_position', ('start_date', 'end_date'), 'current_company']
            ),
        }),
    )
    
    list_display = ('company_name','job_position', 'start_date', 'end_date', 'current_company')
    list_filter = ['job_position']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                ['education_center_name', 'course_name', 'especialty', 'average_grades', ('start_date', 'end_date'), ]
            ),
        }),
    )
    
    list_display = ('course_name', 'average_grades') 
