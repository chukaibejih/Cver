from dataclasses import Field, fields
from rest_framework import serializers
from cv import models

class ResumeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResumeTemplate
        fields = ["name", "template_image", "id"]


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkHistory
        exclude = ["resume"]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        exclude = ["resume"]


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certification
        exclude = ["resume"]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        exclude = ["resume"]

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialLink
        exclude = ["resume"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        exclude = ["resume"]


class ResumeSerializer(serializers.ModelSerializer):
    work_history_set = WorkHistorySerializer(many=True, required=False) 
    education_set = EducationSerializer(many=True, required=False) 
    certification_set = CertificationSerializer(many=True, required=False)
    skill_set = SkillSerializer(many=True, required=False) 
    social_link_set = SocialLinkSerializer(many=True, required=False) 
    project_set = ProjectSerializer(many=True, required=False)

    class Meta:
        model = models.Resume
        fields = (
            "id",
            "user_id",
            "resume_template",
            "job_title",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "professional_summary",
            "work_history_set",
            "certification_set",
            "education_set",
            "skill_set",
            "social_link_set",
            "project_set",
        )
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        work_history_validated_data = validated_data.pop("work_history_set")
        education_validated_data = validated_data.pop("education_set")
        certification_validated_data = validated_data.pop("education_set")
        skill_validated_data = validated_data.pop("skill_set")
        social_link_validated_data = validated_data.pop("social_link_set")
        project_validated_data = validated_data.pop("project")

        work_history_serializer = self.fields["work_history_set"]
        education_serializer = self.fields["education_set"]
        certification_serializer = self.fields["certification_set"]
        skill_serializer = self.fields["skill_set"]
        social_link_serializer = self.fields["social_link_set"]
        project_serializer = self.field["project"]

        resume = models.Resume.objects.create(**validated_data)

        for each in work_history_validated_data:
            each["resume"] = resume
        work_history_serializer.create(work_history_validated_data)

        for each in education_validated_data:
            each["resume"] = resume
        education_serializer.create(education_validated_data)

        for each in certification_validated_data:
            each["resume"] = resume
        certification_serializer.create(certification_validated_data)

        for each in skill_validated_data:
            each["resume"] = resume
        skill_serializer.create(skill_validated_data)

        for each in social_link_validated_data:
            each["resume"] = resume
        social_link_serializer.create(social_link_validated_data)

        for each in project_validated_data:
            each["resume"] = resume
        project_serializer.create(project_validated_data)        

        return resume