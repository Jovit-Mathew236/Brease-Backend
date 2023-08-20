from django.db import models
from db.teams import Teams
from db.user import User


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
    progress = models.IntegerField()
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='updated_by',
                                   related_name='project_updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',
                                   related_name='project_created_by')
    created_at = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'project'

