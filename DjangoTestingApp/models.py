from django.db import models

class JobPosition(models.Model):
    """
    A model that describes a job position in a company.
    """
    position_name = models.CharField(max_length=50)


class JobExperience(models.Model):
    """
    A model that describes a job experience. Includes the position,
    the name of the company and the amount of time you where there.
    """
    
    job_position = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    current_company = models.BooleanField()
