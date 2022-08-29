from django.urls import path
from rest_framework.routers import SimpleRouter

from cv import views

router = SimpleRouter()

router.register("resumes", views.ResumeViewset, basename="resumes")
router.register("templates", views.ResumeTemplateViewset, basename="templates")

urlpatterns = [
    path("download/<int:pk>/", views.ResumePDFView.as_view())
] + router.urls
