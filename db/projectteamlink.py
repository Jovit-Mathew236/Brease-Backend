from django.db import models
from db.projects import Project
from db.teams import Teams


class ProjectTeamLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
