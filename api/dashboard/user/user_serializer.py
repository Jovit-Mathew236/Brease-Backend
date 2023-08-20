from django.db import transaction
from rest_framework import serializers

from db.teams import Teams
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
        ]

    def update(self, instance, validated_data):
        admin = self.context.get("admin")
        current_time = DateTimeUtils.get_current_utc_time()

        with transaction.atomic():
            if isinstance(role_ids := validated_data.pop("roles", None), list):
                instance.user_role_link_user.all().delete()
                UserRoleLink.objects.bulk_create(
                    [
                        UserRoleLink(
                            user=instance,
                            role_id=role_id,
                            created_by=admin,
                            created_at=current_time,
                            verified=True,
                        )
                        for role_id in role_ids
                    ]
                )

            if isinstance(team_ids := validated_data.pop("teams", None), list):
                instance.team_link_user.all().delete()
                Teams.objects.bulk_create(
                    [
                        Teams(
                            user=instance,
                            team_id=team_id,
                            created_by=admin,
                            created_at=current_time,
                        )
                        for team_id in team_ids
                    ]
                )

            return super().update(instance, validated_data)
