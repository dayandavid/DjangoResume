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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
