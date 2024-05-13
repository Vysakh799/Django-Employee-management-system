from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id=models.CharField(max_length=6)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=20)
    phno=models.IntegerField()
    address=models.TextField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    status=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class work(models.Model):
    name=models.TextField()
    end_date=models.DateField()
    start_date=models.DateField()
    def __str__(self):
        return self.name
class assigned_work(models.Model):
    wrk=models.ForeignKey(work,on_delete=models.CASCADE)
    emp=models.ForeignKey(employee,on_delete=models.CASCADE)
    def __str__(self):
        return self.wrk.name

