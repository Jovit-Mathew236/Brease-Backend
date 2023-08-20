from uuid import uuid4
from rest_framework import serializers
from db.projects import Project
from utils.utils import DateTimeUtils

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = 'name', 'description', 'status', 'deadline', 'progress'

class ProjectCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        return Project.objects.create(**validated_data)