# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=45)
    age = models.IntegerField(blank=True, null=True)
    memberid = models.CharField(max_length=45, blank=True, null=True)
    joindate = models.DateTimeField(blank=True, null=True)
    def __str__(self):  # 增加代码
        return self.name   # 增加代码
    
    class Meta:
        managed = False
        db_table = 'members'



    