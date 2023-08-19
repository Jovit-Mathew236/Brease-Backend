from django.db import models


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    deadline = models.DateTimeField()
    progress = models.IntegerField()
    
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'project'
