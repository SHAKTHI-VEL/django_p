from django.db import models

# Create your models here.

# Create your models here.
# Branch
# Team Lead Name
# PRN
# Email(college id)
# Contact Number

# Member2 
# Member3
# Member4

class Team(models.Model):
    id=models.AutoField(primary_key=True)
    branch=models.CharField(max_length=200)
    leadname=models.CharField(max_length=200)
    prn=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    mem1=models.CharField(max_length=200)
    prn1=models.CharField(max_length=200)
    email1=models.CharField(max_length=200)
    contact1=models.CharField(max_length=200)
    mem2=models.CharField(max_length=200)
    prn2=models.CharField(max_length=200)
    email2=models.CharField(max_length=200)
    contact2=models.CharField(max_length=200)
    mem3=models.CharField(max_length=200)
    prn3=models.CharField(max_length=200)
    email3=models.CharField(max_length=200)
    contact3=models.CharField(max_length=200)

    def __str__(self):
        return self.leadname