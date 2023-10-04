from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.conf import settings
# from user.models import Job_Seeker_Cv

class Company_Info(models.Model):
    employer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=100, default="None")
    company_type = models.CharField(max_length=100, default="None")
    industry = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    ntn = models.CharField(max_length=100, blank=True, null=True)
    employer_number = models.CharField(max_length=100, blank=True, null=True)
    operating_since = models.IntegerField(blank=True, null=True)

    # def __str__(self) -> str:
    #     return self.employer.email
    
class Todo_List(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    todo = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return self.employer.email +" > " +self.todo[0:20]+"..."

class Notes_List(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return self.employer.email +" > "+ self.notes[0:20]+"..."
    
class Jobs(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    hiring_number = models.CharField(max_length=100, blank=True, null=True)
    hiring_country = models.CharField(max_length=50)
    hiring_city =  models.CharField(max_length=50)

    status = models.CharField(max_length=50, blank=True, null=True,default="Pending")
    phase = models.CharField(max_length=50, choices=[("Open","Open"),("Close","Close")], default="Open")

    description = models.TextField(blank=True, null=True)

    type = models.CharField(max_length=50, blank=True, null=True)
    salary_rate = models.CharField(max_length=50, blank=True, null=True)
    salary_start_range = models.IntegerField(blank=True, null=True)
    salary_end_range = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title + " - " 
    
class Job_Preferences(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    RESUME_CHOICE = [
        ("Required" , "Required"),
        ("Not Required" , "Not Required"),
        ("Optional" , "Optional"),
    ]

    resume = models.CharField(max_length=50,choices=RESUME_CHOICE, blank=True, null=True)
    send_update_to = models.CharField(max_length=150, blank=True, null=True)
    application_deadline = models.DateField( blank=True, null=True)
    hiring_timeline = models.CharField(max_length=50, blank=True, null=True)


class Job_PreScreen(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    question = models.CharField(max_length=150, blank=True, null=True)
    required = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return self.job.title + self.question

class Job_Reviews(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    email = models.CharField(max_length=50, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    shortlisted_candidate = models.CharField(max_length=50, blank=True, null=True)
    interview_candidate = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.job.title + " - Review"
    
class Application(models.Model):

    job = models.ForeignKey(Jobs, on_delete=models.SET_NULL, null=True, related_name="applications")
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="applications")

    status = models.CharField(max_length=50, choices=[("Pending","Pending"),("Shortlist","Shortlist"),("Interview","Interview"),("Reject","Reject")], default="Pending", null=True, blank=True)
    match = models.CharField(max_length=50, default="0 Star")
    applied_date = models.DateField(auto_now_add=True)

    
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    message = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    



