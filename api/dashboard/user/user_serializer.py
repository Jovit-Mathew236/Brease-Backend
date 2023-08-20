from django.db import transaction
from rest_framework import serializers

from db.teams import Teams,TeamLink
from db.user import User, UserRoleLink
from utils.utils import DateTimeUtils

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "mobile",
            "gender",
            "role",
        ]

    def get_roles(self, obj):
        return [
            user_role_link.role.title
            for user_role_link in obj.user_role_link_user.all()
        ]

class UserDetailsEditSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(write_only=True)
    teams = serializers.CharField(write_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "gender",
            "roles",
            "teams",
            "status",
            "created_at",
        ]

    def create(self, validated_data):
        admin = self.context.get("admin")
        current_time = DateTimeUtils.get_current_utc_time()
        with transaction.atomic():
           roles = validated_data.pop("roles")
           teams = validated_data.pop("teams")
           team = Teams.objects.filter(id=teams).first()
           user = User.objects.create(**validated_data)
           print(team ,type(team)  ,user ,type(user)) 
           TeamLink.objects.create(user=user,team=team ,team_lead=False,created_at=current_time)
           return user