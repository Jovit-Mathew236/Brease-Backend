from rest_framework import serializers

from db.projectteamlink import ProjectTeamLink

class ProjectTeamLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTeamLink
        fields = '__all__'
