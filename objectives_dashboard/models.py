from django.db import models


class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    date_of_innaugration = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'department'


class Keyresults(models.Model):
    keyresult_id = models.CharField(primary_key=True, max_length=12)
    objective = models.ForeignKey('Objectives', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'keyresults'


class Objectives(models.Model):
    objective_id = models.CharField(primary_key=True, max_length=12)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    objective_text = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'objectives'


class Teams(models.Model):
    team_id = models.CharField(primary_key=True, max_length=15)
    team_lead_id = models.CharField(max_length=15, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    average_pay = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teams'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=12)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    team = models.ForeignKey(Teams, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'