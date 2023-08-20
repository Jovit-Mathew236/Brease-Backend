from django.db import models
from db.teams import Teams
from db.user import User


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
    progress = models.IntegerField(default=0, blank=True, null=True)
    team = models.ForeignKey(Teams,models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    