from db.user import User
from django.db import models


class Teams(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, db_column='updated_by',
                                   related_name='learning_circle_updated_by')
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by',
                                   related_name='learning_circle_created_by')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'teams'


class TeamLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    user = models.ForeignKey(User, models.DO_NOTHING)
    circle = models.ForeignKey(Teams, models.DO_NOTHING)
    lead = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_link'