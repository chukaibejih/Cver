from django.shortcuts import render
from django_renderpdf.views import PDFView
from rest_framework import viewsets, permissions, generics
from cv.models import Certification, Project, Resume, ResumeTemplate, WorkHistory, Education, Skill, SocialLink
from cv.serializers import ResumeSerializer, ResumeTemplateSerializer 
from cv.custom_permissions import IsOwnerOrAdmin

# Create your views here.

class ResumeTemplateViewset(viewsets.ModelViewSet):
    """
    list: List all resume templates,
    retrieve: Get a single resume template by ID.
    """

    queryset = ResumeTemplate.objects.all()
    serializer_class = ResumeTemplateSerializer
    http_method_names = ["get"]

class ResumeViewset(viewsets.ModelViewSet):
    """
        list: List all resumes belonging to this authenticated user.
        create: Create a new resume as an authenticated user.
        retrieve: Retrieve resume (by ID) belonging to this authenticated user.
        partial_update: Update resume (by ID) belonging to this authenticated user.
        destroy: Delete resume (by ID) belonging to this authenticated user.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action != "create":
            return [IsOwnerOrAdmin()]
        return super().get_permissions()

    def get_queryset(self):
        try:
            if not self.request.user.is_staff or not self.request.user.is_superuser:
                return Resume.objects.filter(user_id=self.request.user)
        except Exception:
            return Resume.objects.none()
        return super().get_queryset()


class ResumePDFView(PDFView, generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""

        context = super().get_context_data(*args,**kwargs)
        resume = Resume.objects.get(id=kwargs["pk"])

        
        context["resume"] = Resume.objects.get(id=kwargs["pk"])
        context["work_history"] = WorkHistory.objects.filter(
            resume=resume.id
        )
        context["education"] = Education.objects.filter(resume=resume.id)
        context["certification"] = Certification.objects.filter(resume=resume.id)
        context["social_link"] = SocialLink.objects.filter(resume=resume.id)
        context["skills"] = Skill.objects.filter(resume=resume.id)
        context["project"] = Project.objects.filter(resume=resume.id)

        # Gets the template_name dynamically
        self.template_name = f"cv/{context['resume'].resume_template.name}.html"
        # self.download_name = (
        #     f"{context['resume'].resume_template.name}_{context['resume'].first_name}.pdf"
        # )
        # self.prompt_download = True

        return context