from django.db import models


class JobPosition(models.Model):
    """
    A model that describes a job position in a company.
    """
    position_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.position_name


class JobExperience(models.Model):
    """
    A model that describes a job experience. Includes the position,
    the name of the company and the amount of time you where there.
    """
    
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    current_company = models.BooleanField()
    
    def __str__(self):
        return self.company_name
    
    def get_end_date(self):
        """
        If the end date is null is because is the current job.
        """
        if self.current_company:
            return 'Presente'
        else:
            return self.end_date


class Profile(models.Model):
    """
    A model that describes the profile of the user. Name, mail and description.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='profileImages', height_field=None, width_field=None, max_length=None, verbose_name='Profile Picture')
    interest = models.TextField()
    
    def __str__(self):
        return self.first_name


class SocialLink(models.Model):
    """
    A model that describes the link to the social media and the names of the social media.
    """
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    icon = models.CharField( verbose_name='Font Awesome Icon', max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Education(models.Model):
    """
    A model that describes the education of the user
    """
    education_center_name = models.CharField(verbose_name='centro de estudios' ,max_length=50)
    course_name = models.CharField( verbose_name='curso', max_length=50)
    especialty = models.CharField(verbose_name='especialidad', max_length=50)
    average_grades = models.FloatField(verbose_name='promedio')
    start_date = models.DateField(verbose_name='fecha de inicio', auto_now=False, auto_now_add=False)
    end_date = models.DateField(verbose_name='fecha de fin', auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.course_name


class Skill(models.Model):
    """
    A model that describes a skill and selects an icon for the skill
    """
    skill_name = models.CharField(verbose_name='habilidad', max_length=50)
    skill_icon = models.CharField(verbose_name='Icono Font Awesome',max_length=50)
    
    def __str__(self):
        return self.skill_name


class Workflow(models.Model):
    """
    A model that describes the workflows of the user
    """
    workflow_name = models.CharField(max_length=50)
