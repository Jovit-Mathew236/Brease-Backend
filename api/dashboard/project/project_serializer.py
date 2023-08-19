from rest_framework import serializers
from db.projects import Project

class ProjectSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Project
        fields = '__all__'