from django.contrib import admin
from cv import models

# Register your models here.
admin.site.register((
    models.ResumeTemplate,
    models.Resume,
    models.WorkHistory,
    models.Education,
    models.Certification,
    models.Skill,
    models.SocialLink,
    models.Project,
    ))

