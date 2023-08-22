from db.user import User
from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    # priority = models.CharField(max_length=20)
    due_date = models.DateTimeField()
    eta = models.DateTimeField(null=True,blank=True)
    members = models.ManyToManyField(User, through='TaskUserLink')

class TaskUserLink(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
