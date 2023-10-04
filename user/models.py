from django.db import models
from django.contrib.auth.models import User,AbstractUser, Group, Permission
from django.conf import settings


class Seeker_Info(models.Model):
    seeker = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seeker_info")

    date_of_birth  = models.DateField()
    place_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    passport = models.CharField(max_length=50)
    area_of_residence = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.seeker.email + " Detail Info "

class SSL_Info(models.Model):
    seeker = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="ssl_info")
    summary = models.TextField()
    skill = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
        
    def __str__(self) -> str:
        return self.seeker.email
 
    
class Projects(models.Model):
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects")

    role = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

class Employment_Status(models.Model):
    seeker = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    employment_status = models.CharField(max_length=50)
    employment_experience = models.CharField(max_length=50)
    employment_position = models.CharField(max_length=50)    

    seeking_industry = models.CharField(max_length=50)
    seeking_function = models.CharField(max_length=50)
    seeking_position = models.CharField(max_length=50)
    current_salary = models.CharField(max_length=50)
    expected_salary = models.CharField(max_length=50)
    area_of_expertise  = models.CharField(max_length=200)

    
class Experience(models.Model):
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    period_from = models.DateField()
    period_to = models.DateField()

    description = models.CharField(max_length=250)


class Qualification(models.Model):
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="qualification")

    education_level = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    start_period = models.DateField(max_length=50)
    complete_period = models.DateField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self) -> str:
       return self.seeker.email + self.education_level + " in " + self.degree
    

class Seeker_Cv(models.Model):
    seeker = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cv')

    cv_file = models.FileField(upload_to='cv_files/')

    def __str__(self) -> str:
       return self.seeker.email

