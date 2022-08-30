from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from account.models import CustomUser


class ResumeTemplate(models.Model):
    # This holds the resume templates 
    name = models.CharField(max_length=200)
    template_image = models.ImageField(upload_to='resume_samples/')

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        # deletes old template when uploading new template

        try:
            old = ResumeTemplate.objects.get(id=self.id)
            if old.template_image != self.template_image:
                old.template_image.delete(save=False)
        except:
            pass

        super().save(*args, **kwargs)


class Resume(models.Model):
    # Resume model

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resumes')
    job_title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=True)
    email = models.EmailField(max_length=200)
    professional_summary = models.TextField()
    resume_template = models.ForeignKey(ResumeTemplate, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name


class WorkHistory(models.Model):
    # Work History model

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_histories' )
    role = models.CharField(max_length=200)
    job_description = models.TextField()
    employer = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_work_here = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name_plural = 'Work Histories'

    def __str__(self):
        return self.role


class Education(models.Model):
    # Education model

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name= 'education')
    school_name = models.CharField(max_length=200)
    school_location_city = models.CharField(max_length=200)
    school_location_country = CountryField(blank_label='(select country)', default=False) 
    degree = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_attending_here = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return self.degree


class Certification(models.Model):

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=500)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    does_not_expire = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills' )
    name = models.CharField(max_length=200)
    is_soft_skill = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return self.name


class SocialLink(models.Model):
    # social links model (e.g twitter, facebook etc)

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='links' )
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
