from django.db import models
import uuid


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, blank=True, null=True)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'

    @property
    def fullname(self):
        if self.last_name is None:
            return self.first_name

        return f"{self.first_name} {self.last_name}"    
    

class Status(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=75)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='updated_by', related_name='updated_statuses')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='created_by', related_name='created_statuses')
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status' 

class UserStatusLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_status_links')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',related_name='created_user_status_links')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_status_link'           

class Role(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    title = models.CharField(max_length=75)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='updated_by', related_name='updated_roles')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column='created_by', related_name='created_roles')
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'role'    


class UserRoleLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_links')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, db_column='created_by',
                                   related_name='created_user_role_links')
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_role_link'