from db.user import User
from django.db import models


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()


class TeamLink(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    team = models.ForeignKey(Teams, models.DO_NOTHING)
    team_lead = models.BooleanField(default=False)
    created_at = models.DateTimeField()
