from django.db import models

# Create your models here.

class Department(models.Model):
    depid = models.CharField(max_length=3)
    depname = models.CharField(max_length=50)

    def __str__(self):
        return self.depid

class Employee(models.Model):
    empid = models.IntegerField(unique=True)
    empname = models.CharField(max_length=100,unique=True)
    empmail = models.CharField(max_length=100,blank=True)
    depid = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.empname

class Student(models.Model):
    sid = models.IntegerField(unique=True)
    sname = models.CharField(max_length=100)

    def __str__(self):
        return self.sname
